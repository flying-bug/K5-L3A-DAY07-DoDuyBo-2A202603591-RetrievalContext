# Review sheet — A0_dense / test

## t01 (direct) — answered

**Q:** How does the AI RMF define validation?

**Expected:** Validation is the confirmation, through the provision of objective evidence, that the requirements for a specific intended use or application have been fulfilled (ISO 9000:2015).

**Gold:** p18 — "confirmation, through the provision of objective evidence, that the requirements for a specific intended use or application have been fulfilled"

- search `definition of validation in AI RMF` filter=None → p018:para800:04*, p006:para800:01, p012:para800:04 (added 3, dropped 0)

**Answer:** The AI RMF defines validation as the “confirmation, through the provision of objective evidence, that the requirements for a specific intended use or application have been fulfilled” (Source: ISO 9000:2015). This means ensuring that an AI system meets its intended purpose accurately and reliably before deployment. Validation is crucial to avoid deploying AI systems that are inaccurate, unreliable, or poorly generalized, which can increase negative AI risks and reduce trustworthiness [nist-ai-100-1:p018:para800:04].

> **nist-ai-100-1:p018:para800:04** (p18): 3.1 Valid and Reliable Validation is the “confirmation, through the provision of objective evidence, that the requirements for a specific intended use or application have been fulfilled” (Source: ISO 9000:2015). Deployment of AI systems which are inaccurate, unreliable, or poorly generalized to data and settings beyond their training creates and increases negative AI risks and reduces trustworthiness.

Reliability is defined in the same standard as the “ability of an item to perform as required, without failure, for a given time interval, under given conditions” (Source: ISO /IEC TS 5723:2022). Reliability is a goal for overall correctness of AI system operation under the conditions of expected use and over a given period of time, including the entire lifetime of the system.

## t02 (conditional) — answered

**Q:** If an AI risk cannot be measured appropriately, does that mean the AI system is high risk?

**Expected:** No. The inability to appropriately measure AI risks does not imply that the system necessarily poses either a high or a low risk.

**Gold:** p10 — "The inability to appropriately measure AI risks does not imply that an AI system necessarily poses either a high or low risk"

- search `If AI risk cannot be measured appropriately, does it mean the AI system is high risk?` filter={'function': 'MEASURE'} → p035:para800:00, p033:para800:01, p035:para800:02 (added 3, dropped 0)

**Answer:** If AI risks are difficult to assess using currently available measurement techniques or where metrics are not yet available, risk tracking approaches should be considered rather than assuming the AI system is high risk. The inability to measure risk appropriately does not automatically mean the AI system is high risk; instead, it calls for alternative risk tracking methods to identify and monitor risks regularly [nist-ai-100-1:p035:para800:02].

> **nist-ai-100-1:p035:para800:02** (p35): MEASURE 3.1: Approaches, personnel, and documentation are in place to regularly identify and track existing, unanticipated, and emergent AI risks based on factors such as intended and actual performance in deployed contexts.

MEASURE 3.2: Risk tracking approaches are considered for settings where AI risks are difficult to assess using currently available measurement techniques or where metrics are not yet available.

## t03 (filter) — answered

**Q:** Under the GOVERN function, what should be in place to handle failures or incidents in high-risk third-party data or AI systems?

**Expected:** Contingency processes to handle failures or incidents in third-party data or AI systems deemed to be high-risk (GOVERN 6.2).

**Gold:** p29 — "Contingency processes are in place to handle failures or incidents in third-party data or AI systems deemed to be high-risk"

- search `handle failures or incidents in high-risk third-party data or AI systems under GOVERN function` filter={'function': 'GOVERN'} → p029:para800:01*, p028:para800:00, p027:para800:00 (added 3, dropped 0)

**Answer:** Under the GOVERN function, contingency processes must be in place to handle failures or incidents in third-party data or AI systems deemed to be high-risk. Additionally, policies and procedures should address AI risks and benefits arising from third-party software, data, and other supply chain issues, including risks related to third-party intellectual property or other rights [nist-ai-100-1:p029:para800:01].

> **nist-ai-100-1:p029:para800:01** (p29): GOVERN 5.2: Mechanisms are established to enable the team that developed or deployed AI systems to regularly incorporate adjudicated feedback from relevant AI actors into system design and implementation.

GOVERN 6: Policies and procedures are in place to address AI risks and benefits arising from third-party software and data and other supply chain issues.

GOVERN 6.1: Policies and procedures are in place that address AI risks associated with third-party entities, including risks of infringement of a third-party’s intellectual property or other rights.

GOVERN 6.2: Contingency processes are in place to handle failures or incidents in third-party data or AI systems deemed to be high-risk.

## t04 (filter) — answered

**Q:** In the MAP function, what is required of processes for human oversight?

**Expected:** They are defined, assessed, and documented in accordance with organizational policies from the GOVERN function (MAP 3.5).

**Gold:** p32 — "Processes for human oversight are defined, assessed, and documented in accordance with organizational policies from the GOVERN function"

- search `processes for human oversight in MAP function` filter={'function': 'MAP'} → p030:para800:01, p032:para800:01*, p030:para800:00 (added 3, dropped 0)

**Answer:** In the MAP function, processes for human oversight are required to be defined, assessed, and documented in accordance with organizational policies from the GOVERN function [nist-ai-100-1:p032:para800:01].

> **nist-ai-100-1:p032:para800:01** (p32): MAP 3.2: Potential costs, including non-monetary costs, which result from expected or realized AI errors or system functionality and trustworthiness – as connected to organizational risk tolerance – are examined and documented.

MAP 3.3: Targeted application scope is specified and documented based on the system’s capability, established context, and AI system categorization.

MAP 3.4: Processes for operator and practitioner proficiency with AI system performance and trustworthiness – and relevant technical standards and certifications – are defined, assessed, and documented.

MAP 3.5: Processes for human oversight are defined, assessed, and documented in accordance with organizational policies from the GOVERN function.

## t05 (paraphrase) — answered

**Q:** What kind of process for go/no-go decisions on commissioning and deploying a system can Framework users expect to gain?

**Expected:** Explicit processes for making go/no-go system commissioning and deployment decisions.

**Gold:** p24 — "explicit processes for making go/no-go system commissioning and deployment decisions"

- search `process for go/no-go decisions on commissioning and deploying a system` filter={'function': 'MANAGE'} → p036:para800:03, p036:para800:02, p038:para800:00 (added 3, dropped 0)

**Answer:** Framework users can expect to gain a process that includes plans for prioritizing risk, regular monitoring, and improvement after deployment. This process enhances their capacity to manage risks of deployed AI systems and allocate risk management resources based on assessed and prioritized risks. It also involves systematic documentation, mechanisms for assessing emergent risks, and continual improvement, including post-deployment monitoring plans with mechanisms for capturing input from users and other relevant AI actors, incident response, recovery, and change management. This supports informed go/no-go decisions on commissioning and deploying AI systems [nist-ai-100-1:p036:para800:02, nist-ai-100-1:p036:para800:03, nist-ai-100-1:p038:para800:00]. [nist-ai-100-1:p036:para800:02] [nist-ai-100-1:p036:para800:03] [nist-ai-100-1:p038:para800:00]

> **nist-ai-100-1:p036:para800:02** (p36): 5.4 Manage The MANAGE function entails allocating risk resources to mapped and measured risks on a regular basis and as defined by the GOVERN function. Risk treatment comprises plans to respond to, recover from, and communicate about incidents or events.

Contextual information gleaned from expert consultation and input from relevant AI actors – established in GOVERN and carried out in MAP – is utilized in this function to decrease the likelihood of system failures and negative impacts. Systematic documentation practices established in GOVERN and utilized in MAP and MEASURE bolster AI risk management efforts and increase transparency and accountability. Processes for assessing emergent risks are in place, along with mechanisms for continual improvement.

> **nist-ai-100-1:p036:para800:03** (p36): After completing the MANAGE function, plans for prioritizing risk and regular monitoring and improvement will be in place. Framework users will have enhanced capacity to manage the risks of deployed AI systems and to allocate risk management resources based on assessed and prioritized risks. It is incumbent on Framework users to continue to apply the MANAGE function to deployed AI systems as methods, contexts, risks, and needs or expectations from relevant AI actors evolve over time.

> **nist-ai-100-1:p038:para800:00** (p38): Table 4: Categories and subcategories for the MANAGE function. (Continued)

MANAGE 4: Risk treatments, including response and recovery, and communication plans for the identified and measured AI risks are documented and monitored regularly.

MANAGE 4.1: Post-deployment AI system monitoring plans are implemented, including mechanisms for capturing and evaluating input from users and other relevant AI actors, appeal and override, decommissioning, incident response, recovery, and change management.

MANAGE 4.2: Measurable activities for continual improvements are integrated into AI system updates and include regular engagement with interested parties, including relevant AI actors.

## t06 (paraphrase_vi) — answered

**Q:** Theo AI RMF, khi hậu quả nghiêm trọng (ví dụ tính mạng và tự do bị đe dọa), nhà phát triển và bên triển khai AI nên cân nhắc điều gì?

**Expected:** Cân nhắc điều chỉnh các thực hành minh bạch và trách nhiệm giải trình (transparency and accountability) một cách tương xứng và chủ động.

**Gold:** p21 — "AI developers and deployers should consider proportionally and proactively adjusting their transparency and accountability practices"

- search `serious consequences threat to life and liberty developer and deployer considerations` filter={'function': 'MANAGE'} → p036:para800:03, p037:para800:01, p037:para800:02 (added 3, dropped 0)
- search `serious consequences threat to life and liberty risk management considerations developer deployer` filter={'function': 'MANAGE'} → p036:para800:03, p037:para800:01, p037:para800:02 (added 0, dropped 0)

**Answer:** Theo AI RMF, khi hậu quả nghiêm trọng như đe dọa tính mạng và tự do, nhà phát triển và bên triển khai AI nên phát triển, lập kế hoạch và ghi lại các phản ứng đối với các rủi ro AI được đánh giá là ưu tiên cao, bao gồm các lựa chọn giảm thiểu, chuyển giao, tránh hoặc chấp nhận rủi ro. Họ cũng cần lập kế hoạch, chuẩn bị, thực hiện và ghi lại các chiến lược để tối đa hóa lợi ích AI và giảm thiểu tác động tiêu cực, đồng thời xem xét các nguồn lực cần thiết để quản lý rủi ro AI và các phương án thay thế không phải AI nhằm giảm thiểu mức độ hoặc khả năng xảy ra các tác động tiềm tàng. Ngoài ra, cần có các cơ chế để duy trì giá trị của hệ thống AI đã triển khai và các thủ tục để phản ứng và phục hồi khi phát hiện rủi ro chưa biết trước đó, cũng như các cơ chế để ngừng hoặc vô hiệu hóa hệ thống AI khi hiệu suất hoặc kết quả không phù hợp với mục đích sử dụng dự kiến [nist-ai-100-1:p036:para800:03, nist-ai-100-1:p037:para800:01, nist-ai-100-1:p037:para800:02]. [nist-ai-100-1:p036:para800:03] [nist-ai-100-1:p037:para800:01] [nist-ai-100-1:p037:para800:02]

> **nist-ai-100-1:p036:para800:03** (p36): After completing the MANAGE function, plans for prioritizing risk and regular monitoring and improvement will be in place. Framework users will have enhanced capacity to manage the risks of deployed AI systems and to allocate risk management resources based on assessed and prioritized risks. It is incumbent on Framework users to continue to apply the MANAGE function to deployed AI systems as methods, contexts, risks, and needs or expectations from relevant AI actors evolve over time.

> **nist-ai-100-1:p037:para800:01** (p37): MANAGE 1.3: Responses to the AI risks deemed high priority, as identified by the MAP function, are developed, planned, and documented. Risk response options can include mitigating, transferring, avoiding, or accepting.

MANAGE 1.4: Negative residual risks (defined as the sum of all unmitigated risks) to both downstream acquirers of AI systems and end users are documented.

MANAGE 2: Strategies to maximize AI benefits and minimize negative impacts are planned, prepared, implemented, documented, and informed by input from relevant AI actors.

MANAGE 2.1: Resources required to manage AI risks are taken into account – along with viable non-AI alternative systems, approaches, or methods – to reduce the magnitude or likelihood of potential impacts.

> **nist-ai-100-1:p037:para800:02** (p37): MANAGE 2.2: Mechanisms are in place and applied to sustain the value of deployed AI systems.

MANAGE 2.3: Procedures are followed to respond to and recover from a previously unknown risk when it is identified.

MANAGE 2.4: Mechanisms are in place and applied, and responsibilities are assigned and understood, to supersede, disengage, or deactivate AI systems that demonstrate performance or outcomes inconsistent with intended use.

MANAGE 3: AI risks and benefits from third-party entities are managed.

MANAGE 3.1: AI risks and benefits from third-party resources are regularly monitored, and risk controls are applied and documented.

MANAGE 3.2: Pre-trained models which are used for development are monitored as part of AI system regular monitoring and maintenance.

## t07 (direct) — answered

**Q:** What do TEVV tasks for operations involve?

**Expected:** Ongoing monitoring for periodic updates, testing, and SME recalibration of models, tracking of incidents or errors and their management, detection of emergent properties and related impacts, and processes for redress and response.

**Gold:** p41 — "TEVV tasks for operations involve ongoing monitoring for periodic updates, testing, and subject matter expert (SME) recalibration of models"

- search `TEVV tasks for operations` filter={'function': 'MANAGE'} → p038:para800:00, p037:para800:02, p036:para800:02 (added 3, dropped 0)

**Answer:** TEVV tasks for operations involve post-deployment AI system monitoring plans that include mechanisms for capturing and evaluating input from users and other relevant AI actors, appeal and override, decommissioning, incident response, recovery, and change management. These tasks also include measurable activities for continual improvements integrated into AI system updates with regular engagement with interested parties, including relevant AI actors. Additionally, mechanisms are in place to sustain the value of deployed AI systems, respond to and recover from previously unknown risks, and deactivate AI systems that demonstrate inconsistent performance or outcomes. Risk treatments include response, recovery, and communication plans for identified and measured AI risks, which are documented and monitored regularly [nist-ai-100-1:p036:para800:02, nist-ai-100-1:p037:para800:02, nist-ai-100-1:p038:para800:00]. [nist-ai-100-1:p036:para800:02] [nist-ai-100-1:p037:para800:02] [nist-ai-100-1:p038:para800:00]

> **nist-ai-100-1:p036:para800:02** (p36): 5.4 Manage The MANAGE function entails allocating risk resources to mapped and measured risks on a regular basis and as defined by the GOVERN function. Risk treatment comprises plans to respond to, recover from, and communicate about incidents or events.

Contextual information gleaned from expert consultation and input from relevant AI actors – established in GOVERN and carried out in MAP – is utilized in this function to decrease the likelihood of system failures and negative impacts. Systematic documentation practices established in GOVERN and utilized in MAP and MEASURE bolster AI risk management efforts and increase transparency and accountability. Processes for assessing emergent risks are in place, along with mechanisms for continual improvement.

> **nist-ai-100-1:p037:para800:02** (p37): MANAGE 2.2: Mechanisms are in place and applied to sustain the value of deployed AI systems.

MANAGE 2.3: Procedures are followed to respond to and recover from a previously unknown risk when it is identified.

MANAGE 2.4: Mechanisms are in place and applied, and responsibilities are assigned and understood, to supersede, disengage, or deactivate AI systems that demonstrate performance or outcomes inconsistent with intended use.

MANAGE 3: AI risks and benefits from third-party entities are managed.

MANAGE 3.1: AI risks and benefits from third-party resources are regularly monitored, and risk controls are applied and documented.

MANAGE 3.2: Pre-trained models which are used for development are monitored as part of AI system regular monitoring and maintenance.

> **nist-ai-100-1:p038:para800:00** (p38): Table 4: Categories and subcategories for the MANAGE function. (Continued)

MANAGE 4: Risk treatments, including response and recovery, and communication plans for the identified and measured AI risks are documented and monitored regularly.

MANAGE 4.1: Post-deployment AI system monitoring plans are implemented, including mechanisms for capturing and evaluating input from users and other relevant AI actors, appeal and override, decommissioning, incident response, recovery, and change management.

MANAGE 4.2: Measurable activities for continual improvements are integrated into AI system updates and include regular engagement with interested parties, including relevant AI actors.

## t08 (paraphrase) — answered

**Q:** Apart from adopting the AI RMF itself, what does effective AI risk management require from an organization?

**Expected:** Organizational commitment at senior levels; it may also require cultural change within an organization or industry (plus accountability mechanisms, roles, culture and incentives).

**Gold:** p14 — "Effective risk management is realized through organizational commitment at senior levels and may require cultural change within an organization or industry"

- search `effective AI risk management requirements beyond adopting AI RMF` filter=None → p014:para800:00*, p015:para800:01, p047:para800:02 (added 3, dropped 0)

**Answer:** Effective AI risk management requires organizations to establish and maintain appropriate accountability mechanisms, roles and responsibilities, culture, and incentive structures beyond just adopting the AI RMF. It also requires organizational commitment at senior levels and may involve cultural change within the organization or industry. Additionally, successful risk management depends on a sense of collective responsibility among diverse AI actors, involving diverse perspectives, disciplines, professions, and experiences to surface problems and identify risks. These elements are necessary because use of the AI RMF alone will not lead to these changes or provide the appropriate incentives [nist-ai-100-1:p014:para800:00][nist-ai-100-1:p015:para800:01].

> **nist-ai-100-1:p014:para800:00** (p14): Organizations need to establish and maintain the appropriate accountability mechanisms, roles and responsibilities, culture, and incentive structures for risk management to be effective. Use of the AI RMF alone will not lead to these changes or provide the appropriate incentives. Effective risk management is realized through organizational commitment at senior levels and may require cultural change within an organization or industry. In addition, small to medium-sized organizations managing AI risks or implementing the AI RMF may face different challenges than large organizations, depending on their capabilities and resources.

> **nist-ai-100-1:p015:para800:01** (p15): • designate boundaries for AI operation (technical, societal, legal, and ethical); and

• promote discussion of the tradeoffs needed to balance societal values and priorities related to civil liberties and rights, equity, the environment and the planet, and the economy.

Successful risk management depends upon a sense of collective responsibility among AI actors shown in Figure 3. The AI RMF functions, described in Section 5, require diverse perspectives, disciplines, professions, and experiences. Diverse teams contribute to more open sharing of ideas and assumptions about the purposes and functions of technology – making these implicit aspects more explicit. This broader collective perspective creates opportunities for surfacing problems and identifying existing and emergent risks.

## u04 (unanswerable) — abstain

**Q:** What fines does the AI RMF set out under the EU AI Act for non-compliant high-risk AI systems?

**Unanswerable:** AI RMF là khung tự nguyện của NIST, không nhắc EU AI Act hay mức phạt.

- search `fines under EU AI Act for non-compliant high-risk AI systems` filter=None → p037:para800:01, p029:para800:01, p007:para800:02 (added 3, dropped 0)

**Answer:** The retrieved document sections do not specify the fines set out under the EU AI Act for non-compliant high-risk AI systems. More specific information about penalties or fines is missing.

## u05 (unanswerable) — abstain

**Q:** Which specific large language models did NIST evaluate when developing the AI RMF?

**Unanswerable:** Chỉ có 1 lần nhắc 'large language models' (trang 39, ví dụ cross-sectoral profile); không có model nào được NIST đánh giá.

- search `large language models evaluated by NIST for AI RMF development` filter=None → p024:para800:00, p008:para800:02, p047:para800:00 (added 3, dropped 0)

**Answer:** The retrieved document excerpts do not specify which specific large language models NIST evaluated when developing the AI RMF.

## u06 (unanswerable) — abstain

**Q:** Theo AI RMF, chi phí trung bình để một doanh nghiệp vừa và nhỏ triển khai khung này là bao nhiêu?

**Unanswerable:** Trang 14 chỉ nói tổ chức vừa và nhỏ có thể gặp thách thức khác; không có con số chi phí.

- search `average cost for small and medium businesses to implement AI RMF` filter=None → p014:para800:00, p007:para800:02, p007:para800:04 (added 3, dropped 0)

**Answer:** The document mentions that small to medium-sized organizations may face different challenges in managing AI risks or implementing the AI RMF depending on their capabilities and resources, but it does not specify the average cost for these businesses to implement the AI RMF.

