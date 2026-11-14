# Review sheet — A5_dense_rerank_seed / test

## t01 (direct) — answered

**Q:** How does the AI RMF define validation?

**Expected:** Validation is the confirmation, through the provision of objective evidence, that the requirements for a specific intended use or application have been fulfilled (ISO 9000:2015).

**Gold:** p18 — "confirmation, through the provision of objective evidence, that the requirements for a specific intended use or application have been fulfilled"

- search `How does the AI RMF define validation?` filter=None → p006:para800:01, p007:para800:04, p007:para800:02 (added 3, dropped 0)
- search `definition of validation in AI RMF` filter=None → p006:para800:01, p018:para800:04*, p007:para800:02 (added 1, dropped 0)

**Answer:** The AI RMF defines validation as the “confirmation, through the provision of objective evidence, that the requirements for a specific intended use or application have been fulfilled” (Source: ISO 9000:2015). This definition emphasizes ensuring that AI systems meet their intended use to avoid inaccuracies, unreliability, or poor generalization beyond training data, which can increase risks and reduce trustworthiness. [nist-ai-100-1:p018:para800:04]

> **nist-ai-100-1:p018:para800:04** (p18): 3.1 Valid and Reliable Validation is the “confirmation, through the provision of objective evidence, that the requirements for a specific intended use or application have been fulfilled” (Source: ISO 9000:2015). Deployment of AI systems which are inaccurate, unreliable, or poorly generalized to data and settings beyond their training creates and increases negative AI risks and reduces trustworthiness.

Reliability is defined in the same standard as the “ability of an item to perform as required, without failure, for a given time interval, under given conditions” (Source: ISO /IEC TS 5723:2022). Reliability is a goal for overall correctness of AI system operation under the conditions of expected use and over a given period of time, including the entire lifetime of the system.

## t02 (conditional) — answered

**Q:** If an AI risk cannot be measured appropriately, does that mean the AI system is high risk?

**Expected:** No. The inability to appropriately measure AI risks does not imply that the system necessarily poses either a high or a low risk.

**Gold:** p10 — "The inability to appropriately measure AI risks does not imply that an AI system necessarily poses either a high or low risk"

- search `If an AI risk cannot be measured appropriately, does that mean the AI system is high risk?` filter=None → p010:para800:02*, p013:para800:00, p010:para800:03 (added 3, dropped 0)

**Answer:** The inability to appropriately measure AI risks does not imply that an AI system necessarily poses either a high or low risk. Difficulty in measuring risk quantitatively or qualitatively does not automatically categorize the AI system as high risk. Risk measurement challenges exist, but they do not determine the risk level by themselves. Therefore, not being able to measure a risk appropriately does not mean the AI system is high risk [nist-ai-100-1:p010:para800:02].

> **nist-ai-100-1:p010:para800:02** (p10): 1.2.1 Risk Measurement AI risks or failures that are not well-defined or adequately understood are difficult to measure quantitatively or qualitatively. The inability to appropriately measure AI risks does not imply that an AI system necessarily poses either a high or low risk. Some risk measurement challenges include: Risks related to third-party software, hardware, and data: Third-party data or systems can accelerate research and development and facilitate technology transition. They also may complicate risk measurement. Risk can emerge both from third-party data, software or hardware itself and how it is used.

## t03 (filter) — answered

**Q:** Under the GOVERN function, what should be in place to handle failures or incidents in high-risk third-party data or AI systems?

**Expected:** Contingency processes to handle failures or incidents in third-party data or AI systems deemed to be high-risk (GOVERN 6.2).

**Gold:** p29 — "Contingency processes are in place to handle failures or incidents in third-party data or AI systems deemed to be high-risk"

- search `Under the GOVERN function, what should be in place to handle failures or incidents in high-risk third-party data or AI systems?` filter={'function': 'GOVERN'} → p029:para800:01*, p027:para800:00, p029:para800:00 (added 3, dropped 0)

**Answer:** Under the GOVERN function, contingency processes must be in place to handle failures or incidents in third-party data or AI systems deemed to be high-risk. This is specified in GOVERN 6.2, which ensures that organizations have procedures to address such incidents effectively. Additionally, policies and procedures addressing AI risks from third-party software and data, including supply chain issues, should be established as per GOVERN 6 and GOVERN 6.1 [nist-ai-100-1:p029:para800:01].

> **nist-ai-100-1:p029:para800:01** (p29): GOVERN 5.2: Mechanisms are established to enable the team that developed or deployed AI systems to regularly incorporate adjudicated feedback from relevant AI actors into system design and implementation.

GOVERN 6: Policies and procedures are in place to address AI risks and benefits arising from third-party software and data and other supply chain issues.

GOVERN 6.1: Policies and procedures are in place that address AI risks associated with third-party entities, including risks of infringement of a third-party’s intellectual property or other rights.

GOVERN 6.2: Contingency processes are in place to handle failures or incidents in third-party data or AI systems deemed to be high-risk.

## t04 (filter) — answered

**Q:** In the MAP function, what is required of processes for human oversight?

**Expected:** They are defined, assessed, and documented in accordance with organizational policies from the GOVERN function (MAP 3.5).

**Gold:** p32 — "Processes for human oversight are defined, assessed, and documented in accordance with organizational policies from the GOVERN function"

- search `In the MAP function, what is required of processes for human oversight?` filter={'function': 'MAP'} → p032:para800:01*, p030:para800:00, p030:para800:01 (added 3, dropped 0)

**Answer:** In the MAP function, processes for human oversight are required to be defined, assessed, and documented in accordance with organizational policies from the GOVERN function. [nist-ai-100-1:p032:para800:01]

> **nist-ai-100-1:p032:para800:01** (p32): MAP 3.2: Potential costs, including non-monetary costs, which result from expected or realized AI errors or system functionality and trustworthiness – as connected to organizational risk tolerance – are examined and documented.

MAP 3.3: Targeted application scope is specified and documented based on the system’s capability, established context, and AI system categorization.

MAP 3.4: Processes for operator and practitioner proficiency with AI system performance and trustworthiness – and relevant technical standards and certifications – are defined, assessed, and documented.

MAP 3.5: Processes for human oversight are defined, assessed, and documented in accordance with organizational policies from the GOVERN function.

## t05 (paraphrase) — answered

**Q:** What kind of process for go/no-go decisions on commissioning and deploying a system can Framework users expect to gain?

**Expected:** Explicit processes for making go/no-go system commissioning and deployment decisions.

**Gold:** p24 — "explicit processes for making go/no-go system commissioning and deployment decisions"

- search `What kind of process for go/no-go decisions on commissioning and deploying a system can Framework users expect to gain?` filter=None → p030:para800:04, p036:para800:03, p026:para800:01 (added 3, dropped 0)

**Answer:** Framework users can expect to gain a process that provides sufficient contextual knowledge about AI system impacts to inform an initial go/no-go decision about whether to design, develop, or deploy an AI system. This process involves completing the MAP function, followed by utilizing the MEASURE and MANAGE functions along with policies and procedures established in the GOVERN function to assist in AI risk management efforts. The process is iterative and continues as context, capabilities, risks, benefits, and potential impacts evolve over time [nist-ai-100-1:p030:para800:04, nist-ai-100-1:p026:para800:01]. [nist-ai-100-1:p030:para800:04] [nist-ai-100-1:p026:para800:01]

> **nist-ai-100-1:p030:para800:04** (p30): After completing the MAP function, Framework users should have sufficient contextual knowledge about AI system impacts to inform an initial go/no-go decision about whether to design, develop, or deploy an AI system. If a decision is made to proceed, organizations should utilize the MEASURE and MANAGE functions along with policies and procedures put into place in the GOVERN function to assist in AI risk management efforts. It is incumbent on Framework users to continue applying the MAP function to AI systems as context, capabilities, risks, benefits, and potential impacts evolve over time.

Practices related to mapping AI risks are described in the NIST AI RMF Playbook. Table 2 lists the MAP function’s categories and subcategories.

> **nist-ai-100-1:p026:para800:01** (p26): Framework users may apply these functions as best suits their needs for managing AI risks based on their resources and capabilities. Some organizations may choose to select from among the categories and subcategories; others may choose and have the capacity to apply all categories and subcategories. Assuming a governance structure is in place, functions may be performed in any order across the AI lifecycle as deemed to add value by a user of the framework. After instituting the outcomes in GOVERN , most users of the AI RMF would start with the MAP function and continue to MEASURE or MANAGE . However users integrate the functions, the process should be iterative, with cross-referencing between functions as necessary.

## t06 (paraphrase_vi) — answered

**Q:** Theo AI RMF, khi hậu quả nghiêm trọng (ví dụ tính mạng và tự do bị đe dọa), nhà phát triển và bên triển khai AI nên cân nhắc điều gì?

**Expected:** Cân nhắc điều chỉnh các thực hành minh bạch và trách nhiệm giải trình (transparency and accountability) một cách tương xứng và chủ động.

**Gold:** p21 — "AI developers and deployers should consider proportionally and proactively adjusting their transparency and accountability practices"

- search `Theo AI RMF, khi hậu quả nghiêm trọng (ví dụ tính mạng và tự do bị đe dọa), nhà phát triển và bên triển khai AI nên cân nhắc điều gì?` filter=None → p021:para800:01*, p013:para800:00, p009:para800:05 (added 3, dropped 0)

**Answer:** Khi hậu quả nghiêm trọng như tính mạng và tự do bị đe dọa, nhà phát triển và bên triển khai AI nên cân nhắc điều chỉnh các thực hành minh bạch và trách nhiệm một cách tương xứng và chủ động. Họ cũng nên duy trì các thực hành tổ chức và cấu trúc quản trị để giảm thiểu thiệt hại, như quản lý rủi ro, nhằm dẫn đến các hệ thống có trách nhiệm hơn. Nếu mức rủi ro là không chấp nhận được hoặc có nguy cơ nghiêm trọng, việc phát triển và triển khai nên tạm dừng một cách an toàn cho đến khi rủi ro được quản lý đầy đủ [nist-ai-100-1:p021:para800:01][nist-ai-100-1:p013:para800:00].

> **nist-ai-100-1:p021:para800:01** (p21): The role of AI actors should be considered when seeking accountability for the outcomes of AI systems. The relationship between risk and accountability associated with AI and technological systems more broadly differs across cultural, legal, sectoral, and societal contexts. When consequences are severe, such as when life and liberty are at stake, AI developers and deployers should consider proportionally and proactively adjusting their transparency and accountability practices. Maintaining organizational practices and governing structures for harm reduction, like risk management, can help lead to more accountable systems.

> **nist-ai-100-1:p013:para800:00** (p13): When applying the AI RMF, risks which the organization determines to be highest for the AI systems within a given context of use call for the most urgent prioritization and most thorough risk management process. In cases where an AI system presents unacceptable negative risk levels – such as where significant negative impacts are imminent, severe harms are actually occurring, or catastrophic risks are present – development and deployment should cease in a safe manner until risks can be sufficiently managed. If an AI system’s development, deployment, and use cases are found to be low-risk in a specific context, that may suggest potentially lower prioritization.

## t07 (direct) — answered

**Q:** What do TEVV tasks for operations involve?

**Expected:** Ongoing monitoring for periodic updates, testing, and SME recalibration of models, tracking of incidents or errors and their management, detection of emergent properties and related impacts, and processes for redress and response.

**Gold:** p41 — "TEVV tasks for operations involve ongoing monitoring for periodic updates, testing, and subject matter expert (SME) recalibration of models"

- search `What do TEVV tasks for operations involve?` filter=None → p041:para800:01*, p041:para800:00, p040:para800:05 (added 3, dropped 0)

**Answer:** TEVV tasks for operations involve ongoing monitoring for periodic updates, testing, and subject matter expert (SME) recalibration of models, the tracking of incidents or errors reported and their management, the detection of emergent properties and related impacts, and processes for redress and response [nist-ai-100-1:p041:para800:01].

> **nist-ai-100-1:p041:para800:01** (p41): • TEVV tasks for operations involve ongoing monitoring for periodic updates, testing, and subject matter expert (SME) recalibration of models, the tracking of incidents or errors reported and their management, the detection of emergent properties and related impacts, and processes for redress and response.

## t08 (paraphrase) — answered

**Q:** Apart from adopting the AI RMF itself, what does effective AI risk management require from an organization?

**Expected:** Organizational commitment at senior levels; it may also require cultural change within an organization or industry (plus accountability mechanisms, roles, culture and incentives).

**Gold:** p14 — "Effective risk management is realized through organizational commitment at senior levels and may require cultural change within an organization or industry"

- search `Apart from adopting the AI RMF itself, what does effective AI risk management require from an organization?` filter=None → p014:para800:00*, p047:para800:02, p047:para800:01 (added 3, dropped 0)

**Answer:** Effective AI risk management requires organizations to establish and maintain appropriate accountability mechanisms, roles and responsibilities, culture, and incentive structures. It also requires organizational commitment at senior levels and may necessitate cultural change within the organization or industry. Simply adopting the AI RMF is not sufficient to bring about these changes or provide the necessary incentives. Additionally, challenges may vary depending on the size and resources of the organization. These points highlight that effective risk management goes beyond just adopting the AI RMF itself [nist-ai-100-1:p014:para800:00].

> **nist-ai-100-1:p014:para800:00** (p14): Organizations need to establish and maintain the appropriate accountability mechanisms, roles and responsibilities, culture, and incentive structures for risk management to be effective. Use of the AI RMF alone will not lead to these changes or provide the appropriate incentives. Effective risk management is realized through organizational commitment at senior levels and may require cultural change within an organization or industry. In addition, small to medium-sized organizations managing AI risks or implementing the AI RMF may face different challenges than large organizations, depending on their capabilities and resources.

## u04 (unanswerable) — abstain

**Q:** What fines does the AI RMF set out under the EU AI Act for non-compliant high-risk AI systems?

**Unanswerable:** AI RMF là khung tự nguyện của NIST, không nhắc EU AI Act hay mức phạt.

- search `What fines does the AI RMF set out under the EU AI Act for non-compliant high-risk AI systems?` filter=None → p007:para800:02, p013:para800:00, p013:para800:04 (added 3, dropped 0)
- search `EU AI Act fines for non-compliant high-risk AI systems` filter=None → p013:para800:00, p037:para800:01, p029:para800:01 (added 2, dropped 0)
- search `EU AI Act fines non-compliance high-risk AI systems` filter=None → p013:para800:00, p029:para800:01, p007:para800:02 (added 0, dropped 0)

**Answer:** The document does not provide information on fines set out under the EU AI Act for non-compliant high-risk AI systems.

## u05 (unanswerable) — abstain

**Q:** Which specific large language models did NIST evaluate when developing the AI RMF?

**Unanswerable:** Chỉ có 1 lần nhắc 'large language models' (trang 39, ví dụ cross-sectoral profile); không có model nào được NIST đánh giá.

- search `Which specific large language models did NIST evaluate when developing the AI RMF?` filter=None → p024:para800:00, p008:para800:02, p047:para800:00 (added 3, dropped 0)
- search `large language models evaluated by NIST for AI RMF development` filter=None → p008:para800:02, p024:para800:00, p047:para800:01 (added 1, dropped 0)

**Answer:** The document does not specify which specific large language models NIST evaluated when developing the AI RMF.

## u06 (unanswerable) — abstain

**Q:** Theo AI RMF, chi phí trung bình để một doanh nghiệp vừa và nhỏ triển khai khung này là bao nhiêu?

**Unanswerable:** Trang 14 chỉ nói tổ chức vừa và nhỏ có thể gặp thách thức khác; không có con số chi phí.

- search `Theo AI RMF, chi phí trung bình để một doanh nghiệp vừa và nhỏ triển khai khung này là bao nhiêu?` filter=None → p007:para800:02, p014:para800:00, p047:para800:00 (added 3, dropped 0)

**Answer:** The document does not provide specific information on the average cost for a small or medium-sized business to implement the AI RMF.

