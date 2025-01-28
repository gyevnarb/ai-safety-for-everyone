""" This script generates the figures for the paper. """

import sys
import os
import pickle
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import nltk
import wordcloud as wc

from util import load_data, get_counts
from sklearn.feature_extraction.text import TfidfVectorizer


def main():
    """ Runs analyses in paper and produces figures. """
    # Make sure that PDFs are generated with the correct fonts
    mpl.rcParams['pdf.fonttype'] = 42
    mpl.rcParams['ps.fonttype'] = 42
    plt.rc('font', size=11)

    # Load data
    print("Loading data...")
    if not os.path.exists("output"):
        os.mkdir("output")

    if os.path.exists("output/data.p"):
        annotated, references, corpus, dates = pickle.load(open("output/data.p", "rb"))
    else:
        annotated, references, corpus, dates = load_data()
        pickle.dump((annotated, references, corpus, dates), open("output/data.p", "wb"))

    # Generate wordcloud
    print("Generating wordcloud")
    stemmer = nltk.PorterStemmer()
    analyzer = TfidfVectorizer().build_analyzer()
    def stemmed_words(doc):
        return (stemmer.stem(w.lower()) for w in analyzer(doc)
                if w not in nltk.corpus.stopwords.words("english"))
    tfidf_vectorizer = TfidfVectorizer(analyzer=stemmed_words)
    vecs = tfidf_vectorizer.fit_transform(corpus)
    tfidf_scores = pd.DataFrame(vecs.todense().tolist(),
                                columns=tfidf_vectorizer.get_feature_names_out()).T.sum(axis=1)
    print(tfidf_scores.sort_values(ascending=False).head(20))
    wordcloud = wc.WordCloud(width=1000, height=1000, background_color="white",
                             colormap="tab10", random_state=42).generate_from_frequencies(tfidf_scores)
    plt.figure(figsize=(10, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("output/wordcloud.pdf")

    # Generate publication year histogram for riks type analysis
    print("Generating publication year histogram")
    data = []
    for _, ann in annotated.iterrows():
        for risk in ann["risks"]:
            data.append({"year": ann["year"], "risk": risk})
    data = pd.DataFrame.from_records(data)
    years = data.groupby("year")["risk"].value_counts().unstack().fillna(0).astype(int)
    years = years[years.index >= 2015]
    years = years[years.sum(0).sort_values(ascending=False).index]
    plt.figure(figsize=(6, 4.5))
    years.plot(kind="bar", stacked=True, color=mpl.colormaps.get_cmap("tab10").colors, linewidth=2)
    for i, (_, row) in enumerate(years.iterrows()):
        plt.text(i, row.sum() + 0.5, row.sum(), ha="center", va="bottom")
    handles, labels = plt.gca().get_legend_handles_labels()
    order = [7, 6, 5, 4, 3, 2, 1, 0]
    plt.legend(
        [handles[idx] for idx in order],
        [labels[idx] for idx in order],
        title="Risk types",
        bbox_to_anchor=(1, 1),
        frameon=False)
    plt.xlabel("")
    plt.tight_layout()
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig("output/pub-years.pdf")

    # Plot risk type stats
    print("Generating risk type histogram")
    counts = get_counts(annotated["risks"])
    plt.figure(figsize=(6, 4.5))
    counts.plot.barh(color=mpl.colormaps.get_cmap("tab10").colors, width=0.9)
    hatches = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']
    for i, bbar in enumerate(plt.gca().patches):
        bbar.set_hatch(hatches[i % len(hatches)])
    for i, v in enumerate(counts):
        plt.text(v + 0.5, i, f"{v} ({v / counts.sum() * 100:.1f}%)", va="center", ha="left")
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.tight_layout()
    plt.savefig("output/risks.pdf")

    # Plot method type stats
    print("Generating method type comparison")
    params = plt.rcParams.copy()
    sns.set_style("whitegrid")
    plt.rc("font", size=18)
    a = annotated.groupby(["framework", "algorithm"])["type"].value_counts()
    a = a.reset_index()
    g = sns.catplot(a, x="algorithm", y="count", col="type",
                    kind="bar", legend="auto", errorbar=None,
                    sharey=True, sharex=False, palette="tab10", aspect=.75)
    for ax in g.axes.flat:
        for p in ax.patches:
            ax.text(p.get_x() + p.get_width() / 2.,
                    p.get_height() + 0.5, int(p.get_height()), ha="center")
    hatches = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']
    for i, ax in enumerate(g.axes.flat):
        for j, bbar in enumerate(ax.patches):
            bbar.set_hatch(hatches[j % len(hatches)])
    g.set_xlabels("")
    g.set_ylabels("Counts")
    g.set_xticklabels(["No algorithm", "With algorithm"])
    g.axes[0, 0].set_title("Theoretical/No Evaluation")
    g.axes[0, 1].set_title("Applied/Evaluated")
    plt.tight_layout(pad=0.05)
    plt.savefig("output/framework_algo.pdf")
    plt.rcParams = params

    # Get method counts
    print("Generating method type histogram")
    counts = get_counts(annotated["method"])
    counts["analysis\nframework"] += counts["dataset"]
    counts = counts.drop("dataset")
    counts.index = counts.index.str.capitalize()
    sns.set_style("whitegrid")
    plt.figure(figsize=(6, 6))
    counts.plot.barh(color=mpl.colormaps.get_cmap("tab10").colors, width=0.9)
    hatches = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']
    for i, bbar in enumerate(plt.gca().patches):
        bbar.set_hatch(hatches[i % len(hatches)])
    for i, v in enumerate(counts):
        plt.text(v + 0.5, i, f"{v} ({v / counts.sum() * 100:.1f}%)", va="center", ha="left")
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.tight_layout(pad=0.05)
    plt.savefig("output/methods.pdf", bbox_inches="tight")

    return 1


if __name__ == "__main__":
    sys.exit(main())
