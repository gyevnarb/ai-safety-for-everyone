""" Contains functions to map annotation keywords to risk categories
and to map methods to a more readable format. """

def risk_map(risk: str) -> str:
    """ Maps annotation keywords to risk categories.

    Args:
        risk (str): Annotation keyword.

    Returns:
        str: Risk category.
    """

    if risk in ["noise", "outliers", "robustness", "noisy labels", "label noise",
                "input perturbation", "input corruption", "anomaly detection",
                "unseen class", "metric robustness", "out-of-distribution (ood)"]:
        return "Noise and\noutliers"

    elif risk in ["generalization", "non-stationarity", "stability-plasticity",
                  "uncertainty", "partial information", "domain adaptation",
                  "spurious correlation", "domain generalization", "data sampling",
                  "transfer learning"]:
        return "Non-stationary\ndistribution"

    elif "adversarial" in risk or risk in ["misuse", "model poisoning",
                                           "backdoor injection attack",
                                           "synthetic data poisoning", "label poisoning"]:
        return "Adversarial\nattack"

    elif risk in ["unsafe actions", "unsafe exploration",
                  "unsafe states", "exploration", "constraint violation"]:
        return "Unsafe\nexploration"

    elif risk in ["interpretability", "transparency", "standardisation", "machine unlearning"]:
        return "Lack of\nmonitoring"

    elif risk in ["ethical", "bias", "privacy", "social", "economic",
                  "fairness", "responsibility", "psychological", "physical", "biological"]:
        return "Lack of\nmonitoring"

    elif risk in ["unintended behaviour", "emergent behaviour", "hallucination",
                  "reward signal", "deceptive agent", "rogue agent",
                  "reward signal corruption", "transition function corruption",
                  "wireheading", "untruthfulness", "selfish agent", "self-modification"]:
        return "Undesirable\nbehaviour"

    elif risk in ["malware", "phishing", "data sharing", "watermarking"]:
        return "Lack of control\nenforcement"

    elif risk in ["heterogeneous data", "data quality", "multi-modal data",
                  "limited data", "missing data", "data poisoning",
                  "high-dimensional control", "scarce resource allocation"]:
        return "System\nmisspecification"

    elif risk in ["over-the-air updates", "continuous deployment",
                  "new versions", "instability", "retraining"]:
        return "System\nmisspecification"

    elif risk in ["safety verification", "validity", "correctness", "functional safety"]:
        return "Lack of control\nenforcement"

    elif risk in ["model requirements", "problem requirements", "data requirements",
                  "resource constraints", "modeling errors", "domain definition",
                  "capacity limit", "safety requirements", "data efficiency",
                  "system specification", "systemic safety", "hyper-parameter tuning",
                  "communication bottleneck", "standardization"]:
        return "System\nmisspecification"

    elif risk in ["fault", "flash crash", "misclassification",
                  "catastrophic forgetting", "model failure"]:
        return "System\nmisspecification"

    elif risk in ["alignment", "cooperation", "social optimum", "agi"]:
        return "Lack of control\nenforcement"

    elif risk == "holistic":
        return "System\nmisspecification"

    elif risk in ["existential", "singularity"]:
        return "Lack of control\nenforcement"

    else:
        print(risk)
        return risk


def methods_map(kw: str, rl: bool = False) -> str:
    """ Maps method keywords to a more readable format.

    Args:
        kw (str): Method keyword.
        rl (bool): Whether the keyword is related to reinforcement learning.

    Returns:
        str: Nicely formatted method keyword.
    """
    if len(kw) > 12 and " " in kw:
        return kw.replace(" ", "\n")
    if rl and "rl" in kw or kw in ["reinforcement learning"]:
        return "reinforcement learning"

    return kw

responsible_titles = [x.lower() for x in [
    "Toward safe AI",
    "Responsible-AI-by-Design: A Pattern Collection for Designing Responsible Artificial Intelligence Systems",
    "Toward Trustworthy AI: Blockchain-Based Architecture Design for Accountability and Fairness of Federated Learning Systems",
    "Artificial Intelligence Systems, Responsibility and Agential Self-Awareness",
    "Establishing Data Provenance for Responsible Artificial Intelligence Systems",
    "Mind the gaps: Assuring the safety of autonomous systems from an engineering, ethical, and legal perspective",
    "Responsible Agency Through Answerability",
    "Embedding responsibility in intelligent systems: from AI ethics to responsible AI ecosystems",
    "Computational Transcendence: Responsibility and agency",
    "Closing the AI Accountability Gap: Defining an End-to-End Framework for Internal Algorithmic Auditing",
    "Model Checking Human-Agent Collectives for Responsible AI",
    "FairRover: Explorative model building for fair and responsible machine learning",
    "The responsibility gap: Ascribing responsibility for the actions of learning automata",
]]
