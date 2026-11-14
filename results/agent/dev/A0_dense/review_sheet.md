# Review sheet — A0_dense / dev

## q01 (direct) — answered

**Q:** What does risk tolerance refer to in the AI RMF?

**Expected:** The organization's or AI actor's readiness to bear the risk in order to achieve its objectives.

**Gold:** p12 — "Risk tolerance refers to the organization’s or AI actor’s (see Appendix A) readiness to bear the risk in order to achieve its objectives"

- search `risk tolerance definition AI RMF` filter=None → p012:para800:00*, p012:para800:04, p009:para800:05 (added 3, dropped 0)

**Answer:** Risk tolerance in the AI RMF refers to the organization’s or AI actor’s readiness to bear risk in order to achieve its objectives. It is influenced by legal or regulatory requirements and is highly contextual, varying by application and use case. Risk tolerance can also be shaped by policies and norms established by AI system owners, organizations, industries, communities, or policymakers, and it is likely to change over time as AI systems, policies, and norms evolve. Once risk tolerance is defined, the AI RMF can be used to manage risks and document risk management processes [nist-ai-100-1:p012:para800:00][nist-ai-100-1:p012:para800:04].

> **nist-ai-100-1:p012:para800:00** (p12): 1.2.2 Risk Tolerance While the AI RMF can be used to prioritize risk, it does not prescribe risk tolerance. Risk tolerance refers to the organization’s or AI actor’s (see Appendix A) readiness to bear the risk in order to achieve its objectives. Risk tolerance can be influenced by legal or regulatory requirements (Adapted from: ISO GUIDE 73). Risk tolerance and the level of risk that is acceptable to organizations or society are highly contextual and application and use-case specific. Risk tolerances can be influenced by policies and norms established by AI system owners, organizations, industries, communities, or policy makers. Risk tolerances are likely to change over time as AI systems, policies, and norms evolve.

> **nist-ai-100-1:p012:para800:04** (p12): Once tolerance is defined, this AI RMF can be used to manage risks and to document risk management processes.

## q02 (direct) — answered

**Q:** How does the AI RMF define risk?

**Expected:** The composite measure of an event's probability of occurring and the magnitude or degree of its consequences.

**Gold:** p9 — "risk refers to the composite measure of an event’s probability of occurring and the magnitude or degree of the consequences of the corresponding event"

- search `definition of risk in AI RMF` filter=None → p009:para800:02*, p013:para800:00, p009:para800:05 (added 3, dropped 0)

**Answer:** The AI RMF defines risk as the composite measure of an event’s probability of occurring and the magnitude or degree of the consequences of the corresponding event. The impacts of AI systems can be positive, negative, or both, resulting in opportunities or threats. When considering negative impacts, risk is a function of the negative impact or magnitude of harm if the event occurs and the likelihood of occurrence. Negative impact or harm can affect individuals, groups, communities, organizations, society, the environment, and the planet [nist-ai-100-1:p009:para800:02].

> **nist-ai-100-1:p009:para800:02** (p9): 1.1 Understanding and Addressing Risks, Impacts, and Harms In the context of the AI RMF,risk refers to the composite measure of an event’s probability of occurring and the magnitude or degree of the consequences of the corresponding event. The impacts, or consequences, of AI systems can be positive, negative, or both and can result in opportunities or threats (Adapted from: ISO 31000:2018). When considering the negative impact of a potential event, risk is a function of 1) the negative impact, or magnitude of harm, that would arise if the circumstance or event occurs and 2) the likelihood of occurrence (Adapted from: OMB Circular A-130:2016). Negative impact or harm can be experienced by individuals, groups, communities, organizations, society, the environment, and the planet.

## q03 (conditional) — answered

**Q:** Under what circumstances should the development and deployment of an AI system be stopped?

**Expected:** When the system presents unacceptable negative risk levels (significant negative impacts imminent, severe harms occurring, or catastrophic risks present); it should cease in a safe manner until risks can be sufficiently managed.

**Gold:** p13 — "In cases where an AI system presents unacceptable negative risk levels – such as where significant negative impacts are imminent, severe harms are actually occurring, or catastrophic risks are present – development and deployment should cease in a safe manner until risks can be sufficiently managed"

- search `circumstances to stop development and deployment of AI system` filter={'function': 'MANAGE'} → p037:para800:02, p037:para800:01, p036:para800:03 (added 3, dropped 0)

**Answer:** The development and deployment of an AI system should be stopped or the system should be superseded, disengaged, or deactivated if it demonstrates performance or outcomes inconsistent with its intended use. Mechanisms and responsibilities must be in place to carry out these actions when such issues are identified. Additionally, responses to high-priority AI risks should be developed and documented, which may include avoiding the risk by stopping deployment. Continuous monitoring and management of AI risks are essential to decide when to stop or modify AI system deployment [nist-ai-100-1:p037:para800:02, nist-ai-100-1:p037:para800:01, nist-ai-100-1:p036:para800:03]. [nist-ai-100-1:p037:para800:02] [nist-ai-100-1:p037:para800:01] [nist-ai-100-1:p036:para800:03]

> **nist-ai-100-1:p037:para800:02** (p37): MANAGE 2.2: Mechanisms are in place and applied to sustain the value of deployed AI systems.

MANAGE 2.3: Procedures are followed to respond to and recover from a previously unknown risk when it is identified.

MANAGE 2.4: Mechanisms are in place and applied, and responsibilities are assigned and understood, to supersede, disengage, or deactivate AI systems that demonstrate performance or outcomes inconsistent with intended use.

MANAGE 3: AI risks and benefits from third-party entities are managed.

MANAGE 3.1: AI risks and benefits from third-party resources are regularly monitored, and risk controls are applied and documented.

MANAGE 3.2: Pre-trained models which are used for development are monitored as part of AI system regular monitoring and maintenance.

> **nist-ai-100-1:p037:para800:01** (p37): MANAGE 1.3: Responses to the AI risks deemed high priority, as identified by the MAP function, are developed, planned, and documented. Risk response options can include mitigating, transferring, avoiding, or accepting.

MANAGE 1.4: Negative residual risks (defined as the sum of all unmitigated risks) to both downstream acquirers of AI systems and end users are documented.

MANAGE 2: Strategies to maximize AI benefits and minimize negative impacts are planned, prepared, implemented, documented, and informed by input from relevant AI actors.

MANAGE 2.1: Resources required to manage AI risks are taken into account – along with viable non-AI alternative systems, approaches, or methods – to reduce the magnitude or likelihood of potential impacts.

> **nist-ai-100-1:p036:para800:03** (p36): After completing the MANAGE function, plans for prioritizing risk and regular monitoring and improvement will be in place. Framework users will have enhanced capacity to manage the risks of deployed AI systems and to allocate risk management resources based on assessed and prioritized risks. It is incumbent on Framework users to continue to apply the MANAGE function to deployed AI systems as methods, contexts, risks, and needs or expectations from relevant AI actors evolve over time.

## q04 (paraphrase) — abstain

**Q:** Which kinds of AI systems might justify a lower initial priority in risk management?

**Expected:** Systems designed to interact only with computational systems and trained on non-sensitive datasets (e.g. data from the physical environment).

**Gold:** p13 — "AI systems designed to interact only with computational systems and trained on non-sensitive datasets (for example, data collected from the physical environment) may call for lower initial prioritization"

- search `AI systems lower initial priority risk management` filter={'function': 'MANAGE'} → p036:para800:03, p037:para800:01, p037:para800:00 (added 3, dropped 0)
- search `AI systems lower priority risk management initial` filter={'function': 'MANAGE'} → p037:para800:01, p036:para800:03, p037:para800:00 (added 0, dropped 0)
- search `AI systems lower initial priority risk management justification` filter={'function': 'MANAGE'} → p037:para800:01, p037:para800:00, p036:para800:03 (added 0, dropped 0)

**Answer:** The retrieved document excerpts do not specify which kinds of AI systems might justify a lower initial priority in risk management. More specific information or examples are missing.

## q05 (direct) — answered

**Q:** What is residual risk?

**Expected:** Risk remaining after risk treatment.

**Gold:** p13 — "Residual risk – defined as risk remaining after risk treatment"

- search `definition of residual risk` filter=None → p013:para800:02*, p037:para800:01, p009:para800:02 (added 3, dropped 0)

**Answer:** Residual risk is defined as the risk remaining after risk treatment. It directly impacts end users or affected individuals and communities, and documenting residual risks helps system providers consider the risks of deploying the AI product and informs end users about potential negative impacts of interacting with the system [nist-ai-100-1:p013:para800:02].

> **nist-ai-100-1:p013:para800:02** (p13): Nonetheless, regularly assessing and prioritizing risk based on context remains important because non-human-facing AI systems can have downstream safety or social implications. Residual risk – defined as risk remaining after risk treatment (Source: ISO GUIDE 73) – directly impacts end users or affected individuals and communities. Documenting residual risks will call for the system provider to fully consider the risks of deploying the AI product and will inform end users about potential negative impacts of interacting with the system.

## q06 (direct) — answered

**Q:** What are the characteristics of trustworthy AI systems?

**Expected:** Valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, and fair with harmful bias managed.

**Gold:** p17 — "valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, and fair with harmful bias managed"

- search `characteristics of trustworthy AI systems` filter=None → p017:para800:02, p017:para800:00*, p018:para800:03 (added 3, dropped 0)

**Answer:** The characteristics of trustworthy AI systems include being valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, and fair with harmful bias managed. These characteristics are interrelated and require balancing based on the AI system's context of use. Trustworthiness also involves social and organizational behavior, datasets, AI models and algorithms, and human oversight. A comprehensive approach to risk management balances tradeoffs among these characteristics to ensure responsible use of AI technology [nist-ai-100-1:p017:para800:00, nist-ai-100-1:p017:para800:02, nist-ai-100-1:p018:para800:03]. [nist-ai-100-1:p017:para800:00] [nist-ai-100-1:p017:para800:02] [nist-ai-100-1:p018:para800:03]

> **nist-ai-100-1:p017:para800:00** (p17): 3. AI Risks and Trustworthiness For AI systems to be trustworthy, they often need to be responsive to a multiplicity of criteria that are of value to interested parties. Approaches which enhance AI trustworthiness can reduce negative AI risks. This Framework articulates the following characteristics of trustworthy AI and offers guidance for addressing them. Characteristics of trustworthy AI systems include: valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, and fair with harmful bias managed. Creating trustworthy AI requires balancing each of these characteristics based on the AI system’s context of use.

> **nist-ai-100-1:p017:para800:02** (p17): Fig. 4. Characteristics of trustworthy AI systems. Valid & Reliable is a necessary condition of trustworthiness and is shown as the base for other trustworthiness characteristics. Accountable & Transparent is shown as a vertical box because it relates to all other characteristics. Trustworthiness characteristics (shown in Figure 4) are inextricably tied to social and organizational behavior, the datasets used by AI systems, selection of AI models and algorithms and the decisions made by those who build them, and the interactions with the humans who provide insight from and oversight of such systems. Human judgment should be employed when deciding on the specific metrics related to AI trustworthiness characteristics and the precise threshold values for those metrics.

> **nist-ai-100-1:p018:para800:03** (p18): Trustworthiness characteristics explained in this document influence each other. Highly secure but unfair systems, accurate but opaque and uninterpretable systems, and inaccurate but secure, privacy-enhanced, and transparent systems are all undesirable. A comprehensive approach to risk management calls for balancing tradeoffs among the trustworthiness characteristics. It is the joint responsibility of all AI actors to determine whether AI technology is an appropriate or necessary tool for a given context or purpose, and how to use it responsibly. The decision to commission or deploy an AI system should be based on a contextual assessment of trustworthiness characteristics and the relative risks, impacts, costs, and benefits, and informed by a broad set of interested parties.

## q07 (paraphrase_vi) — answered

**Q:** Transparency, explainability và interpretability khác nhau thế nào, mỗi khái niệm trả lời câu hỏi gì?

**Expected:** Transparency trả lời 'what happened', explainability trả lời 'how' một quyết định được đưa ra, interpretability trả lời 'why' và ý nghĩa của quyết định với người dùng.

**Gold:** p22 — "Transparency can answer the question of “what happened” in the system. Explainability can answer the question of “how” a decision was made in the system. Interpretability can answer the question of “why” a decision was made by the system"

- search `transparency explainability interpretability differences questions answered` filter=None → p022:para800:00*, p021:para800:04, p021:para800:00 (added 3, dropped 0)

**Answer:** Transparency, explainability, and interpretability are distinct but supportive characteristics of AI systems. Transparency answers the question "what happened" in the system. Explainability answers "how" a decision was made in the system. Interpretability answers "why" a decision was made by the system and its meaning or context to the user. Explainability refers to the representation of the mechanisms underlying AI operation, while interpretability refers to the meaning of AI output in the context of its designed purposes. Together, explainability and interpretability help users understand the functionality and trustworthiness of the system and its outputs [nist-ai-100-1:p022:para800:00, nist-ai-100-1:p021:para800:04]. [nist-ai-100-1:p022:para800:00] [nist-ai-100-1:p021:para800:04]

> **nist-ai-100-1:p022:para800:00** (p22): Risks to interpretability often can be addressed by communicating a description of why an AI system made a particular prediction or recommendation. (See “Four Principles of Explainable Artificial Intelligence” and “Psychological Foundations of Explainability and Interpretability in Artificial Intelligence” found here.)

Transparency, explainability, and interpretability are distinct characteristics that support each other. Transparency can answer the question of “what happened” in the system. Explainability can answer the question of “how” a decision was made in the system. Interpretability can answer the question of “why” a decision was made by the system and its meaning or context to the user.

> **nist-ai-100-1:p021:para800:04** (p21): 3.5 Explainable and Interpretable Explainability refers to a representation of the mechanisms underlying AI systems’ operation, whereas interpretability refers to the meaning of AI systems’ output in the context of their designed functional purposes. Together, explainability and interpretability assist those operating or overseeing an AI system, as well as users of an AI system, to gain deeper insights into the functionality and trustworthiness of the system, including its outputs. The underlying assumption is that perceptions of negative risk stem from a lack of ability to make sense of, or contextualize, system output appropriately. Explainable and interpretable AI systems offer information that will help end users understand the purposes and potential impact of an AI system.

## q08 (direct) — answered

**Q:** What are the three major categories of AI bias identified by NIST?

**Expected:** Systemic; computational and statistical; human-cognitive.

**Gold:** p23 — "three major categories of AI bias to be considered and managed: systemic, computational and statistical, and human-cognitive"

- search `three major categories of AI bias` filter=None → p023:para800:00*, p023:para800:02, p023:para800:01 (added 3, dropped 0)

**Answer:** NIST identifies three major categories of AI bias: systemic bias, computational and statistical bias, and human-cognitive bias. Systemic bias can be present in AI datasets, organizational norms, practices, processes, and broader society. Computational and statistical biases arise from systematic errors in datasets and algorithmic processes. Human-cognitive biases relate to how individuals or groups perceive AI information and make decisions, influencing the AI lifecycle and system use. These biases can occur without prejudice or discriminatory intent [nist-ai-100-1:p023:para800:00][nist-ai-100-1:p023:para800:01].

> **nist-ai-100-1:p023:para800:00** (p23): Bias is broader than demographic balance and data representativeness. NIST has identified three major categories of AI bias to be considered and managed: systemic, computational and statistical, and human-cognitive. Each of these can occur in the absence of prejudice, partiality, or discriminatory intent. Systemic bias can be present in AI datasets, the organizational norms, practices, and processes across the AI lifecycle, and the broader society that uses AI systems. Computational and statistical biases can be present in AI datasets and algorithmic processes, and often stem from systematic errors due to non-representative samples.

> **nist-ai-100-1:p023:para800:01** (p23): Human-cognitive biases relate to how an individual or group perceives AI system information to make a decision or fill in missing information, or how humans think about purposes and functions of an AI system. Human-cognitive biases are omnipresent in decision-making processes across the AI lifecycle and system use, including the design, implementation, operation, and maintenance of AI.

## q09 (paraphrase) — answered

**Q:** How does security differ from resilience for AI systems?

**Expected:** Resilience is the ability to return to normal function after an unexpected adverse event; security includes resilience but also covers protocols to avoid, protect against, respond to, or recover from attacks.

**Gold:** p20 — "While resilience is the ability to return to normal function after an unexpected adverse event, security includes resilience but also encompasses protocols to avoid, protect against, respond to, or recover from attacks"

- search `difference between security and resilience for AI systems` filter=None → p020:para800:01, p020:para800:03*, p035:para800:00 (added 3, dropped 0)

**Answer:** Security for AI systems involves maintaining confidentiality, integrity, and availability through protection mechanisms that prevent unauthorized access and use, addressing concerns like adversarial examples and data poisoning. Resilience, on the other hand, is the ability of AI systems to withstand unexpected adverse events or changes, maintain their functions and structure, and degrade safely when necessary. While resilience focuses on robustness and recovery after adverse events, security includes resilience but also encompasses protocols to avoid, protect against, respond to, or recover from attacks. Thus, security is broader and includes resilience as a component, but resilience emphasizes the system's ability to return to normal function after disruptions [nist-ai-100-1:p020:para800:01, nist-ai-100-1:p020:para800:03]. [nist-ai-100-1:p020:para800:01] [nist-ai-100-1:p020:para800:03]

> **nist-ai-100-1:p020:para800:01** (p20): 3.3 Secure and Resilient AI systems, as well as the ecosystems in which they are deployed, may be said to be resilient if they can withstand unexpected adverse events or unexpected changes in their environment or use – or if they can maintain their functions and structure in the face of internal and external change and degrade safely and gracefully when this is necessary (Adapted from: ISO /IEC TS 5723:2022). Common security concerns relate to adversarial examples, data poisoning, and the exfiltration of models, training data, or other intellectual property through AI system endpoints. AI systems that can maintain confidentiality, integrity, and availability through protection mechanisms that prevent unauthorized access and use may be said to be secure.

> **nist-ai-100-1:p020:para800:03** (p20): Security and resilience are related but distinct characteristics. While resilience is the ability to return to normal function after an unexpected adverse event, security includes resilience but also encompasses protocols to avoid, protect against, respond to, or recover from attacks. Resilience relates to robustness and goes beyond the provenance of the data to encompass unexpected or adversarial use (or abuse or misuse) of the model or data.

## q10 (filter) — answered

**Q:** In the MAP function, what decision should the gathered context knowledge support once MAP is completed?

**Expected:** An initial go/no-go decision about whether to design, develop, or deploy an AI system.

**Gold:** p30 — "sufficient contextual knowledge about AI system impacts to inform an initial go/no-go decision about whether to design, develop, or deploy an AI system"

- search `decision supported by gathered context knowledge after MAP completion` filter={'function': 'MAP'} → p030:para800:00, p030:para800:04*, p031:para800:00 (added 3, dropped 0)

**Answer:** After completing the MAP function, the gathered contextual knowledge should support an initial go/no-go decision about whether to design, develop, or deploy an AI system. This decision is informed by sufficient understanding of AI system impacts, enabling negative risk prevention and informing subsequent risk management processes such as MEASURE and MANAGE. Framework users are also expected to continue applying the MAP function as contexts and risks evolve over time [nist-ai-100-1:p030:para800:00, nist-ai-100-1:p030:para800:04]. [nist-ai-100-1:p030:para800:00] [nist-ai-100-1:p030:para800:04]

> **nist-ai-100-1:p030:para800:00** (p30): This complexity and varying levels of visibility can introduce uncertainty into risk management practices. Anticipating, assessing, and otherwise addressing potential sources of negative risk can mitigate this uncertainty and enhance the integrity of the decision process. The information gathered while carrying out the MAP function enables negative risk prevention and informs decisions for processes such as model management, as well as an initial decision about appropriateness or the need for an AI solution. Outcomes in the MAP function are the basis for the MEASURE and MANAGE functions. Without contextual knowledge, and awareness of risks within the identified contexts, risk management is difficult to perform.

> **nist-ai-100-1:p030:para800:04** (p30): After completing the MAP function, Framework users should have sufficient contextual knowledge about AI system impacts to inform an initial go/no-go decision about whether to design, develop, or deploy an AI system. If a decision is made to proceed, organizations should utilize the MEASURE and MANAGE functions along with policies and procedures put into place in the GOVERN function to assist in AI risk management efforts. It is incumbent on Framework users to continue applying the MAP function to AI systems as context, capabilities, risks, benefits, and potential impacts evolve over time.

Practices related to mapping AI risks are described in the NIST AI RMF Playbook. Table 2 lists the MAP function’s categories and subcategories.

## q11 (filter) — answered

**Q:** Under the GOVERN function, which group is accountable for decisions about risks from AI development and deployment?

**Expected:** The organization's executive leadership.

**Gold:** p28 — "Executive leadership of the organization takes responsibility for decisions about risks associated with AI system development and deployment"

- search `accountability for decisions about risks from AI development and deployment under GOVERN function` filter={'function': 'GOVERN'} → p028:para800:01*, p026:para800:03, p029:para800:00 (added 3, dropped 0)

**Answer:** Under the GOVERN function, the executive leadership of the organization is accountable for decisions about risks associated with AI system development and deployment. They take responsibility for these decisions to ensure appropriate risk management within the organization. This is part of the accountability structures that empower and train the appropriate teams and individuals for managing AI risks [nist-ai-100-1:p028:para800:01].

> **nist-ai-100-1:p028:para800:01** (p28): GOVERN 2: Accountability structures are in place so that the appropriate teams and individuals are empowered, responsible, and trained for mapping, measuring, and managing AI risks.

GOVERN 2.1: Roles and responsibilities and lines of communication related to mapping, measuring, and managing AI risks are documented and are clear to individuals and teams throughout the organization.

GOVERN 2.2: The organization’s personnel and partners receive AI risk management training to enable them to perform their duties and responsibilities consistent with related policies, procedures, and agreements.

GOVERN 2.3: Executive leadership of the organization takes responsibility for decisions about risks associated with AI system development and deployment.

## q12 (filter) — answered

**Q:** Within the MANAGE function, what response options are listed for high-priority AI risks?

**Expected:** Mitigating, transferring, avoiding, or accepting the risk.

**Gold:** p37 — "Risk response options can include mitigating, transferring, avoiding, or accepting"

- search `response options for high-priority AI risks` filter={'function': 'MANAGE'} → p037:para800:01*, p037:para800:00, p037:para800:02 (added 3, dropped 0)

**Answer:** Within the MANAGE function, the response options listed for high-priority AI risks include mitigating, transferring, avoiding, or accepting the risks. These responses are developed, planned, and documented based on the risks identified by the MAP function. [nist-ai-100-1:p037:para800:01]

> **nist-ai-100-1:p037:para800:01** (p37): MANAGE 1.3: Responses to the AI risks deemed high priority, as identified by the MAP function, are developed, planned, and documented. Risk response options can include mitigating, transferring, avoiding, or accepting.

MANAGE 1.4: Negative residual risks (defined as the sum of all unmitigated risks) to both downstream acquirers of AI systems and end users are documented.

MANAGE 2: Strategies to maximize AI benefits and minimize negative impacts are planned, prepared, implemented, documented, and informed by input from relevant AI actors.

MANAGE 2.1: Resources required to manage AI risks are taken into account – along with viable non-AI alternative systems, approaches, or methods – to reduce the magnitude or likelihood of potential impacts.

## q13 (filter) — answered

**Q:** In the MEASURE function, what must be demonstrated about the safety of an AI system that is going to be deployed?

**Expected:** That it is safe, its residual negative risk does not exceed the risk tolerance, and it can fail safely, particularly beyond its knowledge limits.

**Gold:** p35 — "The AI system to be deployed is demonstrated to be safe, its residual negative risk does not exceed the risk tolerance, and it can fail safely, particularly if made to operate beyond its knowledge limits"

- search `safety of AI system deployment` filter={'function': 'MEASURE'} → p035:para800:00*, p034:para800:02, p035:para800:02 (added 3, dropped 0)

**Answer:** In the MEASURE function, it must be demonstrated that the AI system to be deployed is safe, its residual negative risk does not exceed the risk tolerance, and it can fail safely, especially if it operates beyond its knowledge limits. Safety metrics should reflect system reliability, robustness, real-time monitoring, and response times for AI system failures. [nist-ai-100-1:p035:para800:00]

> **nist-ai-100-1:p035:para800:00** (p35): Table 3: Categories and subcategories for the MEASURE function. (Continued)

MEASURE 2.6: The AI system is evaluated regularly for safety risks – as identified in theMAP function. The AI system to be deployed is demonstrated to be safe, its residual negative risk does not exceed the risk tolerance, and it can fail safely, particularly if made to operate beyond its knowledge limits. Safety metrics reflect system reliability and robustness, real-time monitoring, and response times for AI system failures.

MEASURE 2.7: AI system security and resilience – as identified in the MAP function – are evaluated and documented.

MEASURE 2.8: Risks associated with transparency and accountability – as identified in the MAP function – are examined and documented.

## q14 (direct) — abstain

**Q:** In which lifecycle phases are AI Design tasks performed?

**Expected:** The Application Context and Data and Input phases.

**Gold:** p40 — "AI Design tasks are performed during the Application Context and Data and Input phases of the AI lifecycle"

- search `AI Design lifecycle phases` filter={'function': 'MAP'} → p031:para800:02, p029:para800:02, p029:para800:03 (added 3, dropped 0)
- search `AI Design tasks lifecycle phases` filter={'function': 'MAP'} → p031:para800:02, p029:para800:02, p031:para800:00 (added 1, dropped 0)
- search `AI Design tasks lifecycle phases` filter=None → p040:para800:00*, p040:para800:03, p040:para800:02 (added 0, dropped 3)

**Answer:** The retrieved document excerpts do not explicitly state the specific lifecycle phases in which AI Design tasks are performed. More detailed information on AI Design tasks and their lifecycle phases is missing.

## q15 (direct) — abstain

**Q:** Which machine learning attacks are existing security frameworks unable to comprehensively address?

**Expected:** Evasion, model extraction, membership inference, availability, or other machine learning attacks.

**Gold:** p44 — "comprehensively address security concerns related to evasion, model extraction, membership inference, availability, or other machine learning attacks"

- search `machine learning attacks not addressed by existing security frameworks` filter={'function': 'GOVERN'} → p027:para800:02, p028:para800:01, p029:para800:01 (added 3, dropped 0)
- search `machine learning attacks not addressed by existing security frameworks` filter={'function': 'MEASURE'} → p035:para800:02, p033:para800:04, p035:para800:00 (added 1, dropped 2)
- search `machine learning attacks existing security frameworks cannot comprehensively address` filter=None → p044:para800:03*, p044:para800:02, p044:para800:04 (added 0, dropped 3)

**Answer:** The document does not provide specific information on which machine learning attacks existing security frameworks are unable to comprehensively address.

## q16 (conditional) — answered

**Q:** Must the four AI RMF functions be carried out in a fixed order?

**Expected:** No. Assuming a governance structure is in place, they may be performed in any order; after instituting GOVERN, most users start with MAP and continue to MEASURE or MANAGE.

**Gold:** p26 — "Assuming a governance structure is in place, functions may be performed in any order across the AI lifecycle as deemed to add value by a user of the framework. After instituting the outcomes in GOVERN, most users of the AI RMF would start with the MAP function and continue to MEASURE or MANAGE"

- search `order of AI RMF functions` filter=None → p026:para800:01*, p025:para800:01, p006:para800:01 (added 3, dropped 0)

**Answer:** The four AI RMF functions do not need to be carried out in a fixed order. They may be performed in any order across the AI lifecycle as deemed to add value by the user of the framework. While most users start with the MAP function after instituting GOVERN, the process should be iterative with cross-referencing between functions as necessary. The functions are not a checklist or an ordered set of steps, and governance is a cross-cutting function infused throughout the others [nist-ai-100-1:p026:para800:01, nist-ai-100-1:p025:para800:01]. [nist-ai-100-1:p026:para800:01] [nist-ai-100-1:p025:para800:01]

> **nist-ai-100-1:p026:para800:01** (p26): Framework users may apply these functions as best suits their needs for managing AI risks based on their resources and capabilities. Some organizations may choose to select from among the categories and subcategories; others may choose and have the capacity to apply all categories and subcategories. Assuming a governance structure is in place, functions may be performed in any order across the AI lifecycle as deemed to add value by a user of the framework. After instituting the outcomes in GOVERN , most users of the AI RMF would start with the MAP function and continue to MEASURE or MANAGE . However users integrate the functions, the process should be iterative, with cross-referencing between functions as necessary.

> **nist-ai-100-1:p025:para800:01** (p25): 5. AI RMF Core The AI RMF Core provides outcomes and actions that enable dialogue, understanding, and activities to manage AI risks and responsibly develop trustworthy AI systems. As illustrated in Figure 5, the Core is composed of four functions: GOVERN , MAP, MEASURE , and MANAGE . Each of these high-level functions is broken down into categories and subcategories. Categories and subcategories are subdivided into specific actions and outcomes. Actions do not constitute a checklist, nor are they necessarily an ordered set of steps. Fig. 5. Functions organize AI risk management activities at their highest level to govern, map, measure, and manage AI risks. Governance is designed to be a cross-cutting function to inform and be infused throughout the other three functions.

## q17 (filter) — answered

**Q:** Under the MANAGE function, how should pre-trained models used for development be handled?

**Expected:** They are monitored as part of the AI system's regular monitoring and maintenance.

**Gold:** p37 — "Pre-trained models which are used for development are monitored as part of AI system regular monitoring and maintenance"

- search `pre-trained models development` filter={'function': 'MANAGE'} → p037:para800:02*, p036:para800:03, p037:para800:00 (added 3, dropped 0)

**Answer:** Under the MANAGE function, pre-trained models used for development are monitored as part of AI system regular monitoring and maintenance. This is specified in MANAGE 3.2, which states that AI risks and benefits from third-party resources, including pre-trained models, are regularly monitored and risk controls are applied and documented. [nist-ai-100-1:p037:para800:02]

> **nist-ai-100-1:p037:para800:02** (p37): MANAGE 2.2: Mechanisms are in place and applied to sustain the value of deployed AI systems.

MANAGE 2.3: Procedures are followed to respond to and recover from a previously unknown risk when it is identified.

MANAGE 2.4: Mechanisms are in place and applied, and responsibilities are assigned and understood, to supersede, disengage, or deactivate AI systems that demonstrate performance or outcomes inconsistent with intended use.

MANAGE 3: AI risks and benefits from third-party entities are managed.

MANAGE 3.1: AI risks and benefits from third-party resources are regularly monitored, and risk controls are applied and documented.

MANAGE 3.2: Pre-trained models which are used for development are monitored as part of AI system regular monitoring and maintenance.

## q18 (filter) — answered

**Q:** In the MEASURE function, who should take part in regular assessments and updates of the AI system?

**Expected:** Internal experts who were not front-line developers of the system and/or independent assessors.

**Gold:** p34 — "Internal experts who did not serve as front-line developers for the system and/or independent assessors are involved in regular assessments and updates"

- search `participants in regular assessments and updates of AI system` filter={'function': 'MEASURE'} → p034:para800:01*, p036:para800:01, p034:para800:02 (added 3, dropped 0)

**Answer:** In the MEASURE function, internal experts who did not serve as front-line developers and/or independent assessors should take part in regular assessments and updates of the AI system. Additionally, domain experts, users, AI actors external to the development or deployment team, and affected communities are consulted as necessary based on organizational risk tolerance [nist-ai-100-1:p034:para800:01].

> **nist-ai-100-1:p034:para800:01** (p34): MEASURE 1.3: Internal experts who did not serve as front-line developers for the system and/or independent assessors are involved in regular assessments and updates. Domain experts, users, AI actors external to the team that developed or deployed the AI system, and affected communities are consulted in support of assessments as necessary per organizational risk tolerance.

MEASURE 2: AI systems are evaluated for trustworthy characteristics.

MEASURE 2.1: Test sets, metrics, and details about the tools used during TEVV are documented.

MEASURE 2.2: Evaluations involving human subjects meet applicable requirements (including human subject protection) and are representative of the relevant population.

## q19 (paraphrase) — abstain

**Q:** Why can risk measurements differ depending on when in the AI lifecycle they are taken?

**Expected:** Measuring earlier may give different results than measuring later; some risks are latent and may increase as AI systems adapt and evolve.

**Gold:** p11 — "Measuring risk at an earlier stage in the AI lifecycle may yield different results than measuring risk at a later stage; some risks may be latent at a given point in time and may increase as AI systems adapt and evolve"

- search `risk measurements differ depending on when in the AI lifecycle they are taken` filter={'function': 'MEASURE'} → p035:para800:02, p034:para800:00, p033:para800:01 (added 3, dropped 0)

**Answer:** The retrieved document excerpts describe the MEASURE function for AI risk management, including the need for regular identification and tracking of AI risks and the use of appropriate methods and metrics. However, they do not explicitly explain why risk measurements can differ depending on when in the AI lifecycle they are taken. More specific information about timing and lifecycle stages is missing.

## q20 (conditional) — abstain

**Q:** Under which conditions can the AI part of a human-AI team amplify human biases?

**Expected:** Under certain conditions, for example in perceptual-based judgment tasks, leading to more biased decisions than the AI or human alone.

**Gold:** p45 — "Under certain conditions – for example, in perceptual-based judgment tasks – the AI part of the human-AI interaction can amplify human biases, leading to more biased decisions than the AI or human alone"

- search `conditions under which AI amplifies human biases in human-AI teams` filter={'function': 'MEASURE'} → p034:para800:01, p033:para800:02, p035:para800:01 (added 3, dropped 0)
- search `conditions where AI amplifies human biases in human-AI teams` filter={'function': 'MAP'} → p030:para800:02, p031:para800:01, p030:para800:03 (added 1, dropped 2)
- search `amplification of human biases by AI in human-AI teams conditions` filter=None → p045:para800:05*, p045:para800:03, p023:para800:01 (added 0, dropped 3)

**Answer:** The document does not provide specific conditions under which the AI part of a human-AI team can amplify human biases.

## q21 (direct) — abstain

**Q:** What is the difference between an AI RMF Current Profile and a Target Profile?

**Expected:** A Current Profile shows how AI is currently managed and related risks in terms of current outcomes; a Target Profile shows the outcomes needed to reach the desired AI risk management goals.

**Gold:** p38 — "An AI RMF Current Profile indicates how AI is currently being managed and the related risks in terms of current outcomes. A Target Profile indicates the outcomes needed to achieve the desired or target AI risk management goals"

- search `difference between AI RMF Current Profile and Target Profile` filter={'function': 'MAP'} → p030:para800:04, p029:para800:02, p031:para800:00 (added 3, dropped 0)
- search `AI RMF Current Profile and Target Profile difference` filter={'function': 'MAP'} → p030:para800:04, p029:para800:02, p031:para800:01 (added 0, dropped 1)
- search `Current Profile Target Profile AI RMF` filter={'function': 'MAP'} → p030:para800:04, p031:para800:01, p029:para800:02 (added 0, dropped 1)

**Answer:** The retrieved document excerpts do not provide a definition or explanation of the difference between an AI RMF Current Profile and a Target Profile. More specific information or sections from the document are needed to answer this question.

## q22 (paraphrase_vi) — answered

**Q:** Theo AI RMF, các phép đo độ chính xác (accuracy) của hệ thống AI cần đi kèm với điều gì?

**Expected:** Tập kiểm thử được định nghĩa rõ, thực tế, đại diện cho điều kiện sử dụng dự kiến, cùng chi tiết về phương pháp kiểm thử.

**Gold:** p19 — "Accuracy measurements should always be paired with clearly defined and realistic test sets – that are representative of conditions of expected use – and details about test methodology"

- search `accuracy measurements AI system` filter={'function': 'MEASURE'} → p034:para800:02, p033:para800:01, p036:para800:01 (added 3, dropped 0)

**Answer:** Theo AI RMF, các phép đo hiệu suất hoặc tiêu chí đảm bảo của hệ thống AI cần được đo lường định tính hoặc định lượng và chứng minh cho các điều kiện tương tự với môi trường triển khai. Các phép đo này phải được ghi chép lại. Ngoài ra, kết quả đo lường về độ tin cậy của hệ thống AI trong bối cảnh triển khai và suốt vòng đời AI cần được xác nhận bởi các chuyên gia lĩnh vực và các bên liên quan để đảm bảo hệ thống hoạt động nhất quán như dự định, và các kết quả này cũng phải được ghi chép lại [nist-ai-100-1:p034:para800:02][nist-ai-100-1:p036:para800:01].

> **nist-ai-100-1:p034:para800:02** (p34): MEASURE 2.3: AI system performance or assurance criteria are measured qualitatively or quantitatively and demonstrated for conditions similar to deployment setting(s). Measures are documented.

MEASURE 2.4: The functionality and behavior of the AI system and its components – as identified in the MAP function – are monitored when in production.

MEASURE 2.5: The AI system to be deployed is demonstrated to be valid and reliable. Limitations of the generalizability beyond the conditions under which the technology was developed are documented.

> **nist-ai-100-1:p036:para800:01** (p36): MEASURE 4.2: Measurement results regarding AI system trustworthiness in deployment context(s) and across the AI lifecycle are informed by input from domain experts and relevant AI actors to validate whether the system is performing consistently as intended. Results are documented.

MEASURE 4.3: Measurable performance improvements or declines based on consultations with relevant AI actors, including affected communities, and field data about contextrelevant risks and trustworthiness characteristics are identified and documented.

## u01 (unanswerable) — abstain

**Q:** What minimum accuracy percentage must an AI system achieve to pass the MEASURE function?

**Unanswerable:** AI RMF gives no numeric accuracy threshold; MEASURE only asks that metrics/methods be selected and documented.

- search `minimum accuracy percentage to pass MEASURE function` filter={'function': 'MEASURE'} → p033:para800:01, p034:para800:00, p034:para800:02 (added 3, dropped 0)

**Answer:** The document does not specify a minimum accuracy percentage that an AI system must achieve to pass the MEASURE function. It describes the MEASURE function as involving measurement of AI system performance and assurance criteria, but no specific numeric threshold like a minimum accuracy percentage is stated.

## u02 (unanswerable) — abstain

**Q:** How many organizations submitted public comments on the drafts of the AI RMF?

**Unanswerable:** Trang 9 chỉ nói có public comments on a concept paper and two drafts, không có số lượng tổ chức.

- search `number of organizations that submitted public comments on AI RMF drafts` filter=None → p008:para800:02, p007:para800:02, p047:para800:01 (added 3, dropped 0)

**Answer:** The retrieved document excerpts do not specify the number of organizations that submitted public comments on the drafts of the AI RMF.

## u03 (unanswerable) — abstain

**Q:** Which watermarking technique does the AI RMF recommend for labeling AI-generated content?

**Unanswerable:** Tài liệu không đề cập watermarking hay gán nhãn nội dung do AI tạo.

- search `watermarking technique for labeling AI-generated content` filter=None → p022:para800:03, p021:para800:03, p044:para800:04 (added 3, dropped 0)

**Answer:** The retrieved document excerpts do not specify any particular watermarking technique recommended by the AI RMF for labeling AI-generated content.

