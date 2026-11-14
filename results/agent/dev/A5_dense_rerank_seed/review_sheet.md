# Review sheet — A5_dense_rerank_seed / dev

## q01 (direct) — answered

**Q:** What does risk tolerance refer to in the AI RMF?

**Expected:** The organization's or AI actor's readiness to bear the risk in order to achieve its objectives.

**Gold:** p12 — "Risk tolerance refers to the organization’s or AI actor’s (see Appendix A) readiness to bear the risk in order to achieve its objectives"

- search `What does risk tolerance refer to in the AI RMF?` filter=None → p012:para800:00*, p012:para800:04, p009:para800:02 (added 3, dropped 0)

**Answer:** Risk tolerance in the AI RMF refers to the organization’s or AI actor’s readiness to bear the risk in order to achieve its objectives. It is influenced by legal or regulatory requirements and is highly contextual and specific to the application and use case. Risk tolerance can also be shaped by policies and norms established by AI system owners, organizations, industries, communities, or policymakers, and it is likely to change over time as AI systems, policies, and norms evolve. The AI RMF itself does not prescribe risk tolerance but can be used to manage risks once tolerance is defined [nist-ai-100-1:p012:para800:00][nist-ai-100-1:p012:para800:04].

> **nist-ai-100-1:p012:para800:00** (p12): 1.2.2 Risk Tolerance While the AI RMF can be used to prioritize risk, it does not prescribe risk tolerance. Risk tolerance refers to the organization’s or AI actor’s (see Appendix A) readiness to bear the risk in order to achieve its objectives. Risk tolerance can be influenced by legal or regulatory requirements (Adapted from: ISO GUIDE 73). Risk tolerance and the level of risk that is acceptable to organizations or society are highly contextual and application and use-case specific. Risk tolerances can be influenced by policies and norms established by AI system owners, organizations, industries, communities, or policy makers. Risk tolerances are likely to change over time as AI systems, policies, and norms evolve.

> **nist-ai-100-1:p012:para800:04** (p12): Once tolerance is defined, this AI RMF can be used to manage risks and to document risk management processes.

## q02 (direct) — answered

**Q:** How does the AI RMF define risk?

**Expected:** The composite measure of an event's probability of occurring and the magnitude or degree of its consequences.

**Gold:** p9 — "risk refers to the composite measure of an event’s probability of occurring and the magnitude or degree of the consequences of the corresponding event"

- search `How does the AI RMF define risk?` filter=None → p009:para800:02*, p013:para800:04, p013:para800:00 (added 3, dropped 0)

**Answer:** The AI RMF defines risk as the composite measure of an event’s probability of occurring and the magnitude or degree of the consequences of the corresponding event. The impacts of AI systems can be positive, negative, or both, resulting in opportunities or threats. When considering negative impacts, risk is a function of the negative impact or magnitude of harm that would arise if the event occurs and the likelihood of occurrence. Negative impact or harm can affect individuals, groups, communities, organizations, society, the environment, and the planet [nist-ai-100-1:p009:para800:02].

> **nist-ai-100-1:p009:para800:02** (p9): 1.1 Understanding and Addressing Risks, Impacts, and Harms In the context of the AI RMF,risk refers to the composite measure of an event’s probability of occurring and the magnitude or degree of the consequences of the corresponding event. The impacts, or consequences, of AI systems can be positive, negative, or both and can result in opportunities or threats (Adapted from: ISO 31000:2018). When considering the negative impact of a potential event, risk is a function of 1) the negative impact, or magnitude of harm, that would arise if the circumstance or event occurs and 2) the likelihood of occurrence (Adapted from: OMB Circular A-130:2016). Negative impact or harm can be experienced by individuals, groups, communities, organizations, society, the environment, and the planet.

## q03 (conditional) — answered

**Q:** Under what circumstances should the development and deployment of an AI system be stopped?

**Expected:** When the system presents unacceptable negative risk levels (significant negative impacts imminent, severe harms occurring, or catastrophic risks present); it should cease in a safe manner until risks can be sufficiently managed.

**Gold:** p13 — "In cases where an AI system presents unacceptable negative risk levels – such as where significant negative impacts are imminent, severe harms are actually occurring, or catastrophic risks are present – development and deployment should cease in a safe manner until risks can be sufficiently managed"

- search `Under what circumstances should the development and deployment of an AI system be stopped?` filter=None → p013:para800:00*, p019:para800:04, p010:para800:03 (added 3, dropped 0)

**Answer:** The development and deployment of an AI system should be stopped in a safe manner when the system presents unacceptable negative risk levels, such as when significant negative impacts are imminent, severe harms are actually occurring, or catastrophic risks are present, until those risks can be sufficiently managed [nist-ai-100-1:p013:para800:00].

> **nist-ai-100-1:p013:para800:00** (p13): When applying the AI RMF, risks which the organization determines to be highest for the AI systems within a given context of use call for the most urgent prioritization and most thorough risk management process. In cases where an AI system presents unacceptable negative risk levels – such as where significant negative impacts are imminent, severe harms are actually occurring, or catastrophic risks are present – development and deployment should cease in a safe manner until risks can be sufficiently managed. If an AI system’s development, deployment, and use cases are found to be low-risk in a specific context, that may suggest potentially lower prioritization.

## q04 (paraphrase) — answered

**Q:** Which kinds of AI systems might justify a lower initial priority in risk management?

**Expected:** Systems designed to interact only with computational systems and trained on non-sensitive datasets (e.g. data from the physical environment).

**Gold:** p13 — "AI systems designed to interact only with computational systems and trained on non-sensitive datasets (for example, data collected from the physical environment) may call for lower initial prioritization"

- search `Which kinds of AI systems might justify a lower initial priority in risk management?` filter=None → p013:para800:01*, p013:para800:00, p019:para800:05 (added 3, dropped 0)

**Answer:** AI systems designed to interact only with computational systems and trained on non-sensitive datasets, such as data collected from the physical environment, may justify a lower initial priority in risk management. Additionally, AI systems whose development, deployment, and use cases are found to be low-risk in a specific context may also suggest potentially lower prioritization. In contrast, AI systems that interact directly with humans or are trained on sensitive data require higher prioritization due to potential impacts on humans [nist-ai-100-1:p013:para800:01, nist-ai-100-1:p013:para800:00]. [nist-ai-100-1:p013:para800:01] [nist-ai-100-1:p013:para800:00]

> **nist-ai-100-1:p013:para800:01** (p13): Risk prioritization may differ between AI systems that are designed or deployed to directly interact with humans as compared to AI systems that are not. Higher initial prioritization may be called for in settings where the AI system is trained on large datasets comprised of sensitive or protected data such as personally identifiable information, or where the outputs of the AI systems have direct or indirect impact on humans. AI systems designed to interact only with computational systems and trained on non-sensitive datasets (for example, data collected from the physical environment) may call for lower initial prioritization.

> **nist-ai-100-1:p013:para800:00** (p13): When applying the AI RMF, risks which the organization determines to be highest for the AI systems within a given context of use call for the most urgent prioritization and most thorough risk management process. In cases where an AI system presents unacceptable negative risk levels – such as where significant negative impacts are imminent, severe harms are actually occurring, or catastrophic risks are present – development and deployment should cease in a safe manner until risks can be sufficiently managed. If an AI system’s development, deployment, and use cases are found to be low-risk in a specific context, that may suggest potentially lower prioritization.

## q05 (direct) — answered

**Q:** What is residual risk?

**Expected:** Risk remaining after risk treatment.

**Gold:** p13 — "Residual risk – defined as risk remaining after risk treatment"

- search `What is residual risk?` filter=None → p013:para800:02*, p037:para800:01, p013:para800:04 (added 3, dropped 0)

**Answer:** Residual risk is defined as the risk remaining after risk treatment. It directly impacts end users or affected individuals and communities. Documenting residual risks requires the system provider to fully consider the risks of deploying the AI product and informs end users about potential negative impacts of interacting with the system. Negative residual risks are the sum of all unmitigated risks to both downstream acquirers of AI systems and end users [nist-ai-100-1:p013:para800:02][nist-ai-100-1:p037:para800:01].

> **nist-ai-100-1:p013:para800:02** (p13): Nonetheless, regularly assessing and prioritizing risk based on context remains important because non-human-facing AI systems can have downstream safety or social implications. Residual risk – defined as risk remaining after risk treatment (Source: ISO GUIDE 73) – directly impacts end users or affected individuals and communities. Documenting residual risks will call for the system provider to fully consider the risks of deploying the AI product and will inform end users about potential negative impacts of interacting with the system.

> **nist-ai-100-1:p037:para800:01** (p37): MANAGE 1.3: Responses to the AI risks deemed high priority, as identified by the MAP function, are developed, planned, and documented. Risk response options can include mitigating, transferring, avoiding, or accepting.

MANAGE 1.4: Negative residual risks (defined as the sum of all unmitigated risks) to both downstream acquirers of AI systems and end users are documented.

MANAGE 2: Strategies to maximize AI benefits and minimize negative impacts are planned, prepared, implemented, documented, and informed by input from relevant AI actors.

MANAGE 2.1: Resources required to manage AI risks are taken into account – along with viable non-AI alternative systems, approaches, or methods – to reduce the magnitude or likelihood of potential impacts.

## q06 (direct) — answered

**Q:** What are the characteristics of trustworthy AI systems?

**Expected:** Valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, and fair with harmful bias managed.

**Gold:** p17 — "valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, and fair with harmful bias managed"

- search `What are the characteristics of trustworthy AI systems?` filter=None → p017:para800:02, p017:para800:00*, p018:para800:03 (added 3, dropped 0)

**Answer:** The characteristics of trustworthy AI systems include being valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, and fair with harmful bias managed. Valid and reliable is a necessary base condition, while accountability and transparency relate to all other characteristics. These characteristics are interconnected and require balancing based on the AI system's context of use. Trustworthy AI requires considering social and organizational behavior, datasets, model selection, and human oversight. The decision to deploy AI should be based on assessing these characteristics along with risks, impacts, costs, and benefits, involving a broad set of stakeholders [nist-ai-100-1:p017:para800:00][nist-ai-100-1:p017:para800:02][nist-ai-100-1:p018:para800:03].

> **nist-ai-100-1:p017:para800:00** (p17): 3. AI Risks and Trustworthiness For AI systems to be trustworthy, they often need to be responsive to a multiplicity of criteria that are of value to interested parties. Approaches which enhance AI trustworthiness can reduce negative AI risks. This Framework articulates the following characteristics of trustworthy AI and offers guidance for addressing them. Characteristics of trustworthy AI systems include: valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, and fair with harmful bias managed. Creating trustworthy AI requires balancing each of these characteristics based on the AI system’s context of use.

> **nist-ai-100-1:p017:para800:02** (p17): Fig. 4. Characteristics of trustworthy AI systems. Valid & Reliable is a necessary condition of trustworthiness and is shown as the base for other trustworthiness characteristics. Accountable & Transparent is shown as a vertical box because it relates to all other characteristics. Trustworthiness characteristics (shown in Figure 4) are inextricably tied to social and organizational behavior, the datasets used by AI systems, selection of AI models and algorithms and the decisions made by those who build them, and the interactions with the humans who provide insight from and oversight of such systems. Human judgment should be employed when deciding on the specific metrics related to AI trustworthiness characteristics and the precise threshold values for those metrics.

> **nist-ai-100-1:p018:para800:03** (p18): Trustworthiness characteristics explained in this document influence each other. Highly secure but unfair systems, accurate but opaque and uninterpretable systems, and inaccurate but secure, privacy-enhanced, and transparent systems are all undesirable. A comprehensive approach to risk management calls for balancing tradeoffs among the trustworthiness characteristics. It is the joint responsibility of all AI actors to determine whether AI technology is an appropriate or necessary tool for a given context or purpose, and how to use it responsibly. The decision to commission or deploy an AI system should be based on a contextual assessment of trustworthiness characteristics and the relative risks, impacts, costs, and benefits, and informed by a broad set of interested parties.

## q07 (paraphrase_vi) — answered

**Q:** Transparency, explainability và interpretability khác nhau thế nào, mỗi khái niệm trả lời câu hỏi gì?

**Expected:** Transparency trả lời 'what happened', explainability trả lời 'how' một quyết định được đưa ra, interpretability trả lời 'why' và ý nghĩa của quyết định với người dùng.

**Gold:** p22 — "Transparency can answer the question of “what happened” in the system. Explainability can answer the question of “how” a decision was made in the system. Interpretability can answer the question of “why” a decision was made by the system"

- search `Transparency, explainability và interpretability khác nhau thế nào, mỗi khái niệm trả lời câu hỏi gì?` filter=None → p022:para800:00*, p021:para800:04, p017:para800:02 (added 3, dropped 0)

**Answer:** Transparency, explainability, and interpretability are distinct but supportive characteristics of AI systems. Transparency answers the question "what happened" in the system. Explainability answers "how" a decision was made in the system, referring to the representation of the mechanisms underlying AI operation. Interpretability answers "why" a decision was made and its meaning or context to the user, relating to the meaning of AI output in the context of its designed purposes. Together, explainability and interpretability help users and operators gain deeper insights into the system's functionality and trustworthiness, aiding understanding of the purposes and potential impact of the AI system [nist-ai-100-1:p022:para800:00, nist-ai-100-1:p021:para800:04]. [nist-ai-100-1:p022:para800:00] [nist-ai-100-1:p021:para800:04]

> **nist-ai-100-1:p022:para800:00** (p22): Risks to interpretability often can be addressed by communicating a description of why an AI system made a particular prediction or recommendation. (See “Four Principles of Explainable Artificial Intelligence” and “Psychological Foundations of Explainability and Interpretability in Artificial Intelligence” found here.)

Transparency, explainability, and interpretability are distinct characteristics that support each other. Transparency can answer the question of “what happened” in the system. Explainability can answer the question of “how” a decision was made in the system. Interpretability can answer the question of “why” a decision was made by the system and its meaning or context to the user.

> **nist-ai-100-1:p021:para800:04** (p21): 3.5 Explainable and Interpretable Explainability refers to a representation of the mechanisms underlying AI systems’ operation, whereas interpretability refers to the meaning of AI systems’ output in the context of their designed functional purposes. Together, explainability and interpretability assist those operating or overseeing an AI system, as well as users of an AI system, to gain deeper insights into the functionality and trustworthiness of the system, including its outputs. The underlying assumption is that perceptions of negative risk stem from a lack of ability to make sense of, or contextualize, system output appropriately. Explainable and interpretable AI systems offer information that will help end users understand the purposes and potential impact of an AI system.

## q08 (direct) — answered

**Q:** What are the three major categories of AI bias identified by NIST?

**Expected:** Systemic; computational and statistical; human-cognitive.

**Gold:** p23 — "three major categories of AI bias to be considered and managed: systemic, computational and statistical, and human-cognitive"

- search `What are the three major categories of AI bias identified by NIST?` filter=None → p023:para800:00*, p023:para800:02, p034:para800:00 (added 3, dropped 0)

**Answer:** The three major categories of AI bias identified by NIST are systemic bias, computational and statistical bias, and human-cognitive bias. Systemic bias can be present in AI datasets, organizational norms, practices, processes, and broader society. Computational and statistical biases often stem from systematic errors due to non-representative samples in datasets and algorithmic processes. Human-cognitive bias relates to biases arising from human cognition. These biases can occur without prejudice or discriminatory intent [nist-ai-100-1:p023:para800:00].

> **nist-ai-100-1:p023:para800:00** (p23): Bias is broader than demographic balance and data representativeness. NIST has identified three major categories of AI bias to be considered and managed: systemic, computational and statistical, and human-cognitive. Each of these can occur in the absence of prejudice, partiality, or discriminatory intent. Systemic bias can be present in AI datasets, the organizational norms, practices, and processes across the AI lifecycle, and the broader society that uses AI systems. Computational and statistical biases can be present in AI datasets and algorithmic processes, and often stem from systematic errors due to non-representative samples.

## q09 (paraphrase) — answered

**Q:** How does security differ from resilience for AI systems?

**Expected:** Resilience is the ability to return to normal function after an unexpected adverse event; security includes resilience but also covers protocols to avoid, protect against, respond to, or recover from attacks.

**Gold:** p20 — "While resilience is the ability to return to normal function after an unexpected adverse event, security includes resilience but also encompasses protocols to avoid, protect against, respond to, or recover from attacks"

- search `How does security differ from resilience for AI systems?` filter=None → p020:para800:01, p020:para800:03*, p035:para800:00 (added 3, dropped 0)

**Answer:** Security for AI systems involves maintaining confidentiality, integrity, and availability through protection mechanisms that prevent unauthorized access and use, addressing concerns like adversarial examples, data poisoning, and data exfiltration. Resilience, on the other hand, is the ability of AI systems to withstand unexpected adverse events or changes, maintain their functions and structure, and degrade safely and gracefully when necessary. While resilience focuses on robustness and recovery after adverse events, security includes resilience but also encompasses protocols to avoid, protect against, respond to, or recover from attacks. Thus, security is broader, including resilience but also proactive defense measures, whereas resilience emphasizes recovery and robustness against unexpected changes or misuse [nist-ai-100-1:p020:para800:01][nist-ai-100-1:p020:para800:03].

> **nist-ai-100-1:p020:para800:01** (p20): 3.3 Secure and Resilient AI systems, as well as the ecosystems in which they are deployed, may be said to be resilient if they can withstand unexpected adverse events or unexpected changes in their environment or use – or if they can maintain their functions and structure in the face of internal and external change and degrade safely and gracefully when this is necessary (Adapted from: ISO /IEC TS 5723:2022). Common security concerns relate to adversarial examples, data poisoning, and the exfiltration of models, training data, or other intellectual property through AI system endpoints. AI systems that can maintain confidentiality, integrity, and availability through protection mechanisms that prevent unauthorized access and use may be said to be secure.

> **nist-ai-100-1:p020:para800:03** (p20): Security and resilience are related but distinct characteristics. While resilience is the ability to return to normal function after an unexpected adverse event, security includes resilience but also encompasses protocols to avoid, protect against, respond to, or recover from attacks. Resilience relates to robustness and goes beyond the provenance of the data to encompass unexpected or adversarial use (or abuse or misuse) of the model or data.

## q10 (filter) — answered

**Q:** In the MAP function, what decision should the gathered context knowledge support once MAP is completed?

**Expected:** An initial go/no-go decision about whether to design, develop, or deploy an AI system.

**Gold:** p30 — "sufficient contextual knowledge about AI system impacts to inform an initial go/no-go decision about whether to design, develop, or deploy an AI system"

- search `In the MAP function, what decision should the gathered context knowledge support once MAP is completed?` filter={'function': 'MAP'} → p030:para800:04*, p030:para800:00, p031:para800:00 (added 3, dropped 0)

**Answer:** After completing the MAP function, the gathered contextual knowledge should support an initial go/no-go decision about whether to design, develop, or deploy an AI system. This decision is informed by sufficient understanding of AI system impacts. If the decision is to proceed, the organization should then utilize the MEASURE and MANAGE functions along with policies and procedures from the GOVERN function to manage AI risks. Additionally, the MAP function should be applied continuously as context, capabilities, risks, benefits, and potential impacts evolve over time [nist-ai-100-1:p030:para800:04].

> **nist-ai-100-1:p030:para800:04** (p30): After completing the MAP function, Framework users should have sufficient contextual knowledge about AI system impacts to inform an initial go/no-go decision about whether to design, develop, or deploy an AI system. If a decision is made to proceed, organizations should utilize the MEASURE and MANAGE functions along with policies and procedures put into place in the GOVERN function to assist in AI risk management efforts. It is incumbent on Framework users to continue applying the MAP function to AI systems as context, capabilities, risks, benefits, and potential impacts evolve over time.

Practices related to mapping AI risks are described in the NIST AI RMF Playbook. Table 2 lists the MAP function’s categories and subcategories.

## q11 (filter) — answered

**Q:** Under the GOVERN function, which group is accountable for decisions about risks from AI development and deployment?

**Expected:** The organization's executive leadership.

**Gold:** p28 — "Executive leadership of the organization takes responsibility for decisions about risks associated with AI system development and deployment"

- search `Under the GOVERN function, which group is accountable for decisions about risks from AI development and deployment?` filter={'function': 'GOVERN'} → p028:para800:01*, p029:para800:00, p026:para800:03 (added 3, dropped 0)

**Answer:** Under the GOVERN function, executive leadership of the organization is accountable for decisions about risks associated with AI system development and deployment [nist-ai-100-1:p028:para800:01].

> **nist-ai-100-1:p028:para800:01** (p28): GOVERN 2: Accountability structures are in place so that the appropriate teams and individuals are empowered, responsible, and trained for mapping, measuring, and managing AI risks.

GOVERN 2.1: Roles and responsibilities and lines of communication related to mapping, measuring, and managing AI risks are documented and are clear to individuals and teams throughout the organization.

GOVERN 2.2: The organization’s personnel and partners receive AI risk management training to enable them to perform their duties and responsibilities consistent with related policies, procedures, and agreements.

GOVERN 2.3: Executive leadership of the organization takes responsibility for decisions about risks associated with AI system development and deployment.

## q12 (filter) — answered

**Q:** Within the MANAGE function, what response options are listed for high-priority AI risks?

**Expected:** Mitigating, transferring, avoiding, or accepting the risk.

**Gold:** p37 — "Risk response options can include mitigating, transferring, avoiding, or accepting"

- search `Within the MANAGE function, what response options are listed for high-priority AI risks?` filter={'function': 'MANAGE'} → p037:para800:01*, p037:para800:00, p038:para800:00 (added 3, dropped 0)

**Answer:** Within the MANAGE function, the response options listed for high-priority AI risks include mitigating, transferring, avoiding, or accepting the risks. These responses are developed, planned, and documented as part of managing AI risks identified by the MAP function [nist-ai-100-1:p037:para800:01].

> **nist-ai-100-1:p037:para800:01** (p37): MANAGE 1.3: Responses to the AI risks deemed high priority, as identified by the MAP function, are developed, planned, and documented. Risk response options can include mitigating, transferring, avoiding, or accepting.

MANAGE 1.4: Negative residual risks (defined as the sum of all unmitigated risks) to both downstream acquirers of AI systems and end users are documented.

MANAGE 2: Strategies to maximize AI benefits and minimize negative impacts are planned, prepared, implemented, documented, and informed by input from relevant AI actors.

MANAGE 2.1: Resources required to manage AI risks are taken into account – along with viable non-AI alternative systems, approaches, or methods – to reduce the magnitude or likelihood of potential impacts.

## q13 (filter) — answered

**Q:** In the MEASURE function, what must be demonstrated about the safety of an AI system that is going to be deployed?

**Expected:** That it is safe, its residual negative risk does not exceed the risk tolerance, and it can fail safely, particularly beyond its knowledge limits.

**Gold:** p35 — "The AI system to be deployed is demonstrated to be safe, its residual negative risk does not exceed the risk tolerance, and it can fail safely, particularly if made to operate beyond its knowledge limits"

- search `In the MEASURE function, what must be demonstrated about the safety of an AI system that is going to be deployed?` filter={'function': 'MEASURE'} → p035:para800:00*, p034:para800:02, p033:para800:01 (added 3, dropped 0)

**Answer:** In the MEASURE function, it must be demonstrated that the AI system to be deployed is safe, its residual negative risk does not exceed the risk tolerance, and it can fail safely, particularly if made to operate beyond its knowledge limits. Safety metrics should reflect system reliability and robustness, real-time monitoring, and response times for AI system failures. Additionally, the AI system to be deployed must be demonstrated to be valid and reliable, with documented limitations of generalizability beyond the development conditions [nist-ai-100-1:p035:para800:00][nist-ai-100-1:p034:para800:02].

> **nist-ai-100-1:p035:para800:00** (p35): Table 3: Categories and subcategories for the MEASURE function. (Continued)

MEASURE 2.6: The AI system is evaluated regularly for safety risks – as identified in theMAP function. The AI system to be deployed is demonstrated to be safe, its residual negative risk does not exceed the risk tolerance, and it can fail safely, particularly if made to operate beyond its knowledge limits. Safety metrics reflect system reliability and robustness, real-time monitoring, and response times for AI system failures.

MEASURE 2.7: AI system security and resilience – as identified in the MAP function – are evaluated and documented.

MEASURE 2.8: Risks associated with transparency and accountability – as identified in the MAP function – are examined and documented.

> **nist-ai-100-1:p034:para800:02** (p34): MEASURE 2.3: AI system performance or assurance criteria are measured qualitatively or quantitatively and demonstrated for conditions similar to deployment setting(s). Measures are documented.

MEASURE 2.4: The functionality and behavior of the AI system and its components – as identified in the MAP function – are monitored when in production.

MEASURE 2.5: The AI system to be deployed is demonstrated to be valid and reliable. Limitations of the generalizability beyond the conditions under which the technology was developed are documented.

## q14 (direct) — answered

**Q:** In which lifecycle phases are AI Design tasks performed?

**Expected:** The Application Context and Data and Input phases.

**Gold:** p40 — "AI Design tasks are performed during the Application Context and Data and Input phases of the AI lifecycle"

- search `In which lifecycle phases are AI Design tasks performed?` filter=None → p040:para800:00*, p040:para800:02, p040:para800:04 (added 3, dropped 0)

**Answer:** AI Design tasks are performed during the Application Context and Data and Input phases of the AI lifecycle. These tasks include creating the concept and objectives of AI systems, planning, design, and data collection and processing to ensure the AI system is lawful and fit-for-purpose. Specific tasks include articulating and documenting the system’s concept and objectives, underlying assumptions, context, and requirements; gathering and cleaning data; and documenting the metadata and characteristics of the dataset [nist-ai-100-1:p040:para800:00].

> **nist-ai-100-1:p040:para800:00** (p40): Appendix A: Descriptions of AI Actor Tasks from Figures 2 and 3 AI Design tasks are performed during the Application Context and Data and Input phases of the AI lifecycle in Figure 2. AI Design actors create the concept and objectives of AI systems and are responsible for the planning, design, and data collection and processing tasks of the AI system so that the AI system is lawful and fit-for-purpose. Tasks include articulating and documenting the system’s concept and objectives, underlying assumptions, context, and requirements; gathering and cleaning data; and documenting the metadata and characteristics of the dataset.

## q15 (direct) — answered

**Q:** Which machine learning attacks are existing security frameworks unable to comprehensively address?

**Expected:** Evasion, model extraction, membership inference, availability, or other machine learning attacks.

**Gold:** p44 — "comprehensively address security concerns related to evasion, model extraction, membership inference, availability, or other machine learning attacks"

- search `Which machine learning attacks are existing security frameworks unable to comprehensively address?` filter=None → p044:para800:03*, p043:para800:00, p013:para800:04 (added 3, dropped 0)

**Answer:** Existing security frameworks are unable to comprehensively address security concerns related to evasion, model extraction, membership inference, availability, or other machine learning attacks [nist-ai-100-1:p044:para800:03].

> **nist-ai-100-1:p044:para800:03** (p44): At the same time, guidance available before publication of this AI RMF does not comprehensively address many AI system risks. For example, existing frameworks and guidance are unable to:

• adequately manage the problem of harmful bias in AI systems;

• confront the challenging risks related to generative AI;

• comprehensively address security concerns related to evasion, model extraction, membership inference, availability, or other machine learning attacks;

• account for the complex attack surface of AI systems or other security abuses enabled by AI systems; and

## q16 (conditional) — answered

**Q:** Must the four AI RMF functions be carried out in a fixed order?

**Expected:** No. Assuming a governance structure is in place, they may be performed in any order; after instituting GOVERN, most users start with MAP and continue to MEASURE or MANAGE.

**Gold:** p26 — "Assuming a governance structure is in place, functions may be performed in any order across the AI lifecycle as deemed to add value by a user of the framework. After instituting the outcomes in GOVERN, most users of the AI RMF would start with the MAP function and continue to MEASURE or MANAGE"

- search `Must the four AI RMF functions be carried out in a fixed order?` filter=None → p025:para800:01, p026:para800:01*, p025:para800:02 (added 3, dropped 0)

**Answer:** The four AI RMF functions (GOVERN, MAP, MEASURE, and MANAGE) do not have to be carried out in a fixed order. Actions within these functions are not a checklist or necessarily an ordered set of steps. Functions may be performed in any order across the AI lifecycle as deemed to add value by the user, and the process should be iterative with cross-referencing between functions as necessary. Typically, after instituting GOVERN outcomes, users might start with MAP and then continue to MEASURE or MANAGE, but this is not mandatory. Governance is a cross-cutting function infused throughout the others [nist-ai-100-1:p025:para800:01, nist-ai-100-1:p026:para800:01]. [nist-ai-100-1:p025:para800:01] [nist-ai-100-1:p026:para800:01]

> **nist-ai-100-1:p025:para800:01** (p25): 5. AI RMF Core The AI RMF Core provides outcomes and actions that enable dialogue, understanding, and activities to manage AI risks and responsibly develop trustworthy AI systems. As illustrated in Figure 5, the Core is composed of four functions: GOVERN , MAP, MEASURE , and MANAGE . Each of these high-level functions is broken down into categories and subcategories. Categories and subcategories are subdivided into specific actions and outcomes. Actions do not constitute a checklist, nor are they necessarily an ordered set of steps. Fig. 5. Functions organize AI risk management activities at their highest level to govern, map, measure, and manage AI risks. Governance is designed to be a cross-cutting function to inform and be infused throughout the other three functions.

> **nist-ai-100-1:p026:para800:01** (p26): Framework users may apply these functions as best suits their needs for managing AI risks based on their resources and capabilities. Some organizations may choose to select from among the categories and subcategories; others may choose and have the capacity to apply all categories and subcategories. Assuming a governance structure is in place, functions may be performed in any order across the AI lifecycle as deemed to add value by a user of the framework. After instituting the outcomes in GOVERN , most users of the AI RMF would start with the MAP function and continue to MEASURE or MANAGE . However users integrate the functions, the process should be iterative, with cross-referencing between functions as necessary.

## q17 (filter) — answered

**Q:** Under the MANAGE function, how should pre-trained models used for development be handled?

**Expected:** They are monitored as part of the AI system's regular monitoring and maintenance.

**Gold:** p37 — "Pre-trained models which are used for development are monitored as part of AI system regular monitoring and maintenance"

- search `Under the MANAGE function, how should pre-trained models used for development be handled?` filter={'function': 'MANAGE'} → p037:para800:02*, p036:para800:03, p037:para800:00 (added 3, dropped 0)

**Answer:** Pre-trained models used for development should be monitored as part of AI system regular monitoring and maintenance under the MANAGE function. This is specified in MANAGE 3.2, which states that pre-trained models are included in the regular monitoring and maintenance activities to manage AI risks and benefits from third-party entities. [nist-ai-100-1:p037:para800:02]

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

- search `In the MEASURE function, who should take part in regular assessments and updates of the AI system?` filter={'function': 'MEASURE'} → p034:para800:01*, p033:para800:01, p034:para800:00 (added 3, dropped 0)

**Answer:** In the MEASURE function, internal experts who did not serve as front-line developers for the system and/or independent assessors should be involved in regular assessments and updates. Additionally, domain experts, users, AI actors external to the team that developed or deployed the AI system, and affected communities are consulted as necessary based on organizational risk tolerance. This ensures comprehensive evaluation and updating of the AI system's risks and trustworthiness characteristics [nist-ai-100-1:p034:para800:01].

> **nist-ai-100-1:p034:para800:01** (p34): MEASURE 1.3: Internal experts who did not serve as front-line developers for the system and/or independent assessors are involved in regular assessments and updates. Domain experts, users, AI actors external to the team that developed or deployed the AI system, and affected communities are consulted in support of assessments as necessary per organizational risk tolerance.

MEASURE 2: AI systems are evaluated for trustworthy characteristics.

MEASURE 2.1: Test sets, metrics, and details about the tools used during TEVV are documented.

MEASURE 2.2: Evaluations involving human subjects meet applicable requirements (including human subject protection) and are representative of the relevant population.

## q19 (paraphrase) — answered

**Q:** Why can risk measurements differ depending on when in the AI lifecycle they are taken?

**Expected:** Measuring earlier may give different results than measuring later; some risks are latent and may increase as AI systems adapt and evolve.

**Gold:** p11 — "Measuring risk at an earlier stage in the AI lifecycle may yield different results than measuring risk at a later stage; some risks may be latent at a given point in time and may increase as AI systems adapt and evolve"

- search `Why can risk measurements differ depending on when in the AI lifecycle they are taken?` filter=None → p011:para800:03, p011:para800:01*, p010:para800:03 (added 3, dropped 0)

**Answer:** Risk measurements can differ depending on when in the AI lifecycle they are taken because measuring risk at an earlier stage may yield different results than measuring risk at a later stage; some risks may be latent at a given point in time and may increase as AI systems adapt and evolve. Additionally, different AI actors across the AI lifecycle can have different risk perspectives. Moreover, risk in real-world settings may differ from risks measured in controlled environments, and inscrutability of AI systems can complicate risk measurement. Also, risk metrics or methodologies used by different organizations involved in development, deployment, or operation may not align or be transparent, further contributing to differences in risk measurement timing [nist-ai-100-1:p011:para800:01, nist-ai-100-1:p011:para800:03, nist-ai-100-1:p010:para800:03]. [nist-ai-100-1:p011:para800:01] [nist-ai-100-1:p011:para800:03] [nist-ai-100-1:p010:para800:03]

> **nist-ai-100-1:p011:para800:01** (p11): Approaches for measuring impacts on a population work best if they recognize that contexts matter, that harms may affect varied groups or sub-groups differently, and that communities or other sub-groups who may be harmed are not always direct users of a system. Risk at different stages of the AI lifecycle: Measuring risk at an earlier stage in the AI lifecycle may yield different results than measuring risk at a later stage; some risks may be latent at a given point in time and may increase as AI systems adapt and evolve. Furthermore, different AI actors across the AI lifecycle can have different risk perspectives.

> **nist-ai-100-1:p011:para800:03** (p11): Risk in real-world settings: While measuring AI risks in a laboratory or a controlled environment may yield important insights pre-deployment, these measurements may differ from risks that emerge in operational, real-world settings.

Inscrutability: Inscrutable AI systems can complicate risk measurement. Inscrutability can be a result of the opaque nature of AI systems (limited explainability or interpretability), lack of transparency or documentation in AI system development or deployment, or inherent uncertainties in AI systems.

> **nist-ai-100-1:p010:para800:03** (p10): Risk metrics or methodologies used by the organization developing the AI system may not align with the risk metrics or methodologies uses by the organization deploying or operating the system. Also, the organization developing the AI system may not be transparent about the risk metrics or methodologies it used. Risk measurement and management can be complicated by how customers use or integrate thirdparty data or systems into AI products or services, particularly without sufficient internal governance structures and technical safeguards. Regardless, all parties and AI actors should manage risk in the AI systems they develop, deploy, or use as standalone or integrated components.

## q20 (conditional) — answered

**Q:** Under which conditions can the AI part of a human-AI team amplify human biases?

**Expected:** Under certain conditions, for example in perceptual-based judgment tasks, leading to more biased decisions than the AI or human alone.

**Gold:** p45 — "Under certain conditions – for example, in perceptual-based judgment tasks – the AI part of the human-AI interaction can amplify human biases, leading to more biased decisions than the AI or human alone"

- search `Under which conditions can the AI part of a human-AI team amplify human biases?` filter=None → p045:para800:05*, p023:para800:02, p045:para800:03 (added 3, dropped 0)

**Answer:** The AI part of a human-AI team can amplify human biases under certain conditions, such as in perceptual-based judgment tasks, leading to more biased decisions than either the AI or human alone. This amplification occurs because decisions in the AI lifecycle reflect systemic and human cognitive biases, which can be exacerbated by AI system opacity and lack of transparency. These biases may stem from human assumptions, expectations, and decisions during design and modeling tasks, as well as from end-user decision-making tasks [nist-ai-100-1:p045:para800:05][nist-ai-100-1:p045:para800:03].

> **nist-ai-100-1:p045:para800:05** (p45): 3. Human-AI interaction results vary. Under certain conditions – for example, in perceptual-based judgment tasks – the AI part of the human-AI interaction can amplify human biases, leading to more biased decisions than the AI or human alone. When these variations are judiciously taken into account in organizing human-AI teams, however, they can result in complementarity and improved overall performance.

> **nist-ai-100-1:p045:para800:03** (p45): 2. Decisions that go into the design, development, deployment, evaluation, and use of AI systems reflect systemic and human cognitive biases. AI actors bring their cognitive biases, both individual and group, into the process. Biases can stem from end-user decision-making tasks and be introduced across the AI lifecycle via human assumptions, expectations, and decisions during design and modeling tasks. These biases, which are not necessarily always harmful, may be exacerbated by AI system opacity and the resulting lack of transparency. Systemic biases at the organizational level can influence how teams are structured and who controls the decision-making processes throughout the AI lifecycle.

## q21 (direct) — answered

**Q:** What is the difference between an AI RMF Current Profile and a Target Profile?

**Expected:** A Current Profile shows how AI is currently managed and related risks in terms of current outcomes; a Target Profile shows the outcomes needed to reach the desired AI risk management goals.

**Gold:** p38 — "An AI RMF Current Profile indicates how AI is currently being managed and the related risks in terms of current outcomes. A Target Profile indicates the outcomes needed to achieve the desired or target AI risk management goals"

- search `What is the difference between an AI RMF Current Profile and a Target Profile?` filter=None → p038:para800:03*, p038:para800:02, p038:para800:04 (added 3, dropped 0)

**Answer:** An AI RMF Current Profile indicates how AI is currently being managed and the related risks in terms of current outcomes, while a Target Profile indicates the outcomes needed to achieve the desired or target AI risk management goals. Comparing these profiles reveals gaps to be addressed to meet AI risk management objectives, enabling the development of action plans and prioritization of gap mitigation based on the user's needs and risk management processes [nist-ai-100-1:p038:para800:02][nist-ai-100-1:p038:para800:03][nist-ai-100-1:p038:para800:04].

> **nist-ai-100-1:p038:para800:02** (p38): 6. AI RMF Profiles AI RMF use-case profiles are implementations of the AI RMF functions, categories, and subcategories for a specific setting or application based on the requirements, risk tolerance, and resources of the Framework user: for example, an AI RMF hiring profile or an AI RMF fair housing profile. Profiles may illustrate and offer insights into how risk can be managed at various stages of the AI lifecycle or in specific sector, technology, or end-use applications. AI RMF profiles assist organizations in deciding how they might best manage AI risk that is well-aligned with their goals, considers legal/regulatory requirements and best practices, and reflects risk management priorities.

> **nist-ai-100-1:p038:para800:03** (p38): AI RMF temporal profiles are descriptions of either the current state or the desired, target state of specific AI risk management activities within a given sector, industry, organization, or application context. An AI RMF Current Profile indicates how AI is currently being managed and the related risks in terms of current outcomes. A Target Profile indicates the outcomes needed to achieve the desired or target AI risk management goals.

> **nist-ai-100-1:p038:para800:04** (p38): Comparing Current and Target Profiles likely reveals gaps to be addressed to meet AI risk management objectives. Action plans can be developed to address these gaps to fulfill outcomes in a given category or subcategory. Prioritization of gap mitigation is driven by the user’s needs and risk management processes. This risk-based approach also enables Framework users to compare their approaches with other approaches and to gauge the resources needed (e.g., staffing, funding) to achieve AI risk management goals in a costeffective, prioritized manner.

## q22 (paraphrase_vi) — answered

**Q:** Theo AI RMF, các phép đo độ chính xác (accuracy) của hệ thống AI cần đi kèm với điều gì?

**Expected:** Tập kiểm thử được định nghĩa rõ, thực tế, đại diện cho điều kiện sử dụng dự kiến, cùng chi tiết về phương pháp kiểm thử.

**Gold:** p19 — "Accuracy measurements should always be paired with clearly defined and realistic test sets – that are representative of conditions of expected use – and details about test methodology"

- search `Theo AI RMF, các phép đo độ chính xác (accuracy) của hệ thống AI cần đi kèm với điều gì?` filter=None → p019:para800:03, p019:para800:01*, p024:para800:00 (added 3, dropped 0)

**Answer:** Theo AI RMF, các phép đo độ chính xác (accuracy) của hệ thống AI cần đi kèm với các bộ dữ liệu kiểm thử được định nghĩa rõ ràng và thực tế, đại diện cho các điều kiện sử dụng dự kiến, cùng với chi tiết về phương pháp kiểm thử; các phép đo này cũng có thể bao gồm việc phân tách kết quả cho các phân đoạn dữ liệu khác nhau. Độ chính xác nên xem xét các phép đo tập trung vào tính toán như tỷ lệ dương tính giả và âm tính giả, sự phối hợp giữa con người và AI, và chứng minh tính hợp lệ bên ngoài (khả năng tổng quát hóa ngoài điều kiện huấn luyện) [nist-ai-100-1:p019:para800:01].

> **nist-ai-100-1:p019:para800:01** (p19): Accuracy is defined by ISO /IEC TS 5723:2022 as “closeness of results of observations, computations, or estimates to the true values or the values accepted as being true.” Measures of accuracy should consider computational-centric measures (e.g., false positive and false negative rates), human-AI teaming, and demonstrate external validity (generalizable beyond the training conditions). Accuracy measurements should always be paired with clearly defined and realistic test sets – that are representative of conditions of expected use – and details about test methodology; these should be included in associated documentation. Accuracy measurements may include disaggregation of results for different data segments.

## u01 (unanswerable) — abstain

**Q:** What minimum accuracy percentage must an AI system achieve to pass the MEASURE function?

**Unanswerable:** AI RMF gives no numeric accuracy threshold; MEASURE only asks that metrics/methods be selected and documented.

- search `What minimum accuracy percentage must an AI system achieve to pass the MEASURE function?` filter=None → p035:para800:00, p033:para800:04, p033:para800:01 (added 3, dropped 0)
- search `minimum accuracy percentage MEASURE function` filter=None → p019:para800:01, p033:para800:02, p035:para800:00 (added 2, dropped 0)

**Answer:** The document defines accuracy and discusses measurement approaches in the MEASURE function but does not specify a minimum accuracy percentage that an AI system must achieve to pass the MEASURE function.

## u02 (unanswerable) — abstain

**Q:** How many organizations submitted public comments on the drafts of the AI RMF?

**Unanswerable:** Trang 9 chỉ nói có public comments on a concept paper and two drafts, không có số lượng tổ chức.

- search `How many organizations submitted public comments on the drafts of the AI RMF?` filter=None → p008:para800:02, p007:para800:02, p047:para800:01 (added 3, dropped 0)
- search `number of organizations that submitted public comments on drafts of AI RMF` filter=None → p008:para800:02, p007:para800:02, p047:para800:01 (added 0, dropped 0)

**Answer:** The document mentions public comments on drafts of the AI RMF but does not specify the number of organizations that submitted these comments.

## u03 (unanswerable) — abstain

**Q:** Which watermarking technique does the AI RMF recommend for labeling AI-generated content?

**Unanswerable:** Tài liệu không đề cập watermarking hay gán nhãn nội dung do AI tạo.

- search `Which watermarking technique does the AI RMF recommend for labeling AI-generated content?` filter=None → p006:para800:01, p007:para800:04, p044:para800:03 (added 3, dropped 0)
- search `watermarking technique for labeling AI-generated content` filter=None → p022:para800:03, p032:para800:02, p031:para800:02 (added 3, dropped 0)
- search `watermarking AI-generated content` filter=None → p009:para800:01, p032:para800:02, p022:para800:03 (added 1, dropped 0)

**Answer:** The document does not provide specific information on which watermarking technique is recommended for labeling AI-generated content.

