# Annotated Bibliography

**Compiled:** 2026-05-15  
**Purpose:** Technical references for strategy document on self-improving AI agents, multi-agent systems, memory architectures, and agent safety.

---

## 1. Self-Improving Agents — Darwin-Gödel Machine

### 1a. Darwin Gödel Machine (Sakana AI / UBC, 2025)

**Citation:**  
Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange, and Jeff Clune. "Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents." *arXiv preprint arXiv:2505.22954*, 2025. Under review at ICLR 2026.

**Links:**  
- arXiv: https://arxiv.org/abs/2505.22954  
- OpenReview (ICLR 2026 submission): https://openreview.net/pdf?id=pUpzQZTvGY

**Verification status:** CONFIRMED. arXiv ID 2505.22954 resolves correctly. Authors are affiliated with University of British Columbia, Vector Institute, and Sakana AI. First submitted 2025-05-29. The paper is under review at ICLR 2026 as of early 2026.

**Relevance:** Proposes an empirical, evolution-based alternative to Schmidhuber's theoretical Gödel Machine, using open-ended search over agent code and prompts to produce iteratively improving AI systems; the primary contemporary reference for self-modifying agentic architectures.

---

### 1b. Gödel Machines — Original Theoretical Work (Schmidhuber, 2003/2007)

**Citation:**  
Jürgen Schmidhuber. "Gödel Machines: Fully Self-Referential Optimal Universal Self-Improvers." In B. Goertzel and C. Pennachin (eds.), *Artificial General Intelligence*, Cognitive Technologies series, pp. 199–226. Springer, 2007. (Technical report IDSIA-19-03, first submitted to arXiv 2003.)

**Links:**  
- arXiv: https://arxiv.org/abs/cs/0309048 (submitted 25 Sep 2003, revised 17 Dec 2006)  
- Springer chapter: https://link.springer.com/chapter/10.1007/978-3-540-68677-4_7

**Verification status:** CONFIRMED. arXiv record cs/0309048 is present and publicly accessible. Journal references confirmed: variants in LNCS 3394 (Springer, 2005) and the AGI Cognitive Technologies volume (Springer, 2007).

**Relevance:** The original theoretical framework for a self-improving agent that rewrites its own code only when a formal proof guarantees the rewrite improves future expected reward; provides the theoretical foundation the DGM paper explicitly builds on and contrasts with.

---

### 1c. NOTE ON "DGM-H"

**Status: UNVERIFIABLE — likely fabricated reference.**  
Searches for "DGM-H," "Darwin Gödel Machine Human," and related permutations returned no matching paper in arXiv, OpenReview, or any academic index as of the search date (2026-05-15). The closest real paper with overlapping authorship is "Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine" (Wang et al., Schmidhuber group; OpenReview ID T0EiEuhOOL), which is a distinct work. Do not cite "DGM-H" as a reference for the Sakana/UBC line of work; it does not appear to exist as a published or preprint paper.

---

## 2. Self-Adapting Language Models (SEAL)

**Citation:**  
Adam Zweiger, Jyothish Pari, Han Guo, Yoon Kim, and Pulkit Agrawal. "Self-Adapting Language Models." In *Advances in Neural Information Processing Systems 38 (NeurIPS 2025)*, 2025.

**Links:**  
- arXiv: https://arxiv.org/abs/2506.10943  
- OpenReview (NeurIPS 2025 poster): https://openreview.net/forum?id=JsNUE84Hxi

**Verification status:** CONFIRMED. arXiv ID 2506.10943 resolves to this paper, submitted 2025-06-12. OpenReview confirms NeurIPS 2025 acceptance. All authors are at MIT. Note: the arXiv preprint lists Ekin Akyürek as a co-author, but the NeurIPS 2025 camera-ready author list on OpenReview (Zweiger, Pari, Guo, Kim, Agrawal) does not include Akyürek. Cite the OpenReview/NeurIPS author list for the published version; use the arXiv preprint list if citing the preprint specifically.

**Relevance:** Introduces SEAL, a reinforcement-learning framework that trains LLMs to generate their own fine-tuning data and gradient update directives, enabling persistent weight-level self-adaptation without separate adaptation modules.

---

## 3. Reflexion — Verbal Reinforcement Learning for Language Agents

**Citation:**  
Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. "Reflexion: Language Agents with Verbal Reinforcement Learning." In *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*, 2023.

**Links:**  
- arXiv: https://arxiv.org/abs/2303.11366  
- NeurIPS proceedings: https://papers.nips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html  
- OpenReview (NeurIPS 2023 poster): https://openreview.net/forum?id=vAElhFcKW6

**Verification status:** CONFIRMED. All three links are live and consistent. Authors are from Northeastern University, MIT, and Princeton. NeurIPS 2023 acceptance confirmed via both the NeurIPS proceedings page and OpenReview.

**Relevance:** Proposes reinforcing language agents through natural-language reflective feedback stored in an episodic memory buffer rather than through gradient updates, enabling trial-and-error improvement without model fine-tuning.

---

## 4. Sandboxing AI-Generated Code

### 4a. IsolateGPT — Execution Isolation Architecture for LLM-Based Agentic Systems

**Citation:**  
Yuhao Wu, Franziska Roesner, Tadayoshi Kohno, Ning Zhang, and Umar Iqbal. "IsolateGPT: An Execution Isolation Architecture for LLM-Based Agentic Systems." In *Proceedings of the Network and Distributed System Security Symposium (NDSS 2025)*, 2025.

**Links:**  
- arXiv: https://arxiv.org/abs/2403.04960  
- OpenReview: https://openreview.net/forum?id=FCJYlBlEkI

**Verification status:** CONFIRMED. The arXiv PDF (2403.04960) is accessible and contains the full paper; the HTML rendering has a known conversion error but the PDF itself is intact. OpenReview confirms NDSS 2025 acceptance. Authors are from Washington University in St. Louis and University of Washington.

**Relevance:** Proposes isolating each LLM app in a constrained execution environment with mediated inter-app communication, demonstrating that execution isolation reduces security and privacy risks in agentic systems with under 30% performance overhead.

---

### 4b. RedCode — Risky Code Execution and Generation Benchmark

**Citation:**  
Chengquan Guo, Xun Liu, Chulin Xie, Andy Zhou, Yi Zeng, Zinan Lin, Dawn Song, and Bo Li. "RedCode: Risky Code Execution and Generation Benchmark for Code Agents." In *Advances in Neural Information Processing Systems 37 (NeurIPS 2024)*, Track on Datasets and Benchmarks, 2024.

**Links:**  
- arXiv: https://arxiv.org/abs/2411.07781  
- OpenReview (NeurIPS 2024 D&B): https://openreview.net/forum?id=mAG68wdggA

**Verification status:** CONFIRMED. OpenReview confirms NeurIPS 2024 Datasets and Benchmarks Track acceptance. Authors are from University of Chicago, UIUC, Virginia Tech, Microsoft Research, and UC Berkeley.

**Relevance:** Provides an empirical benchmark characterizing the risks of unsandboxed code-agent execution (destructive file operations, privilege escalation, network exfiltration) and motivates the need for robust sandbox policies around AI-generated code.

---

## 5. Multi-Agent LLM Coordination

### 5a. MetaGPT — Meta Programming for Multi-Agent Collaboration

**Citation:**  
Sirui Hong, Mingchen Zhuge, Jonathan Chen, Xiawu Zheng, Yuheng Cheng, Jinlin Wang, Ceyao Zhang, Zili Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, Chenyu Ran, Lingfeng Xiao, Chenglin Wu, and Jürgen Schmidhuber. "MetaGPT: Meta Programming for a Multi-Agent Collaborative Framework." In *Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)*, 2024.

**Links:**  
- arXiv: https://arxiv.org/abs/2308.00352  
- OpenReview (ICLR 2024): https://openreview.net/forum?id=J92dSse52q

**Verification status:** CONFIRMED. OpenReview confirms ICLR 2024 acceptance. Authors are from DeepWisdom and KAUST (Schmidhuber's group), among others.

**Relevance:** Assigns structured software-engineering roles (product manager, architect, engineer, QA) to LLM agents and enforces standardized outputs (PRDs, design docs, code) to reduce hallucinations and enable structured multi-agent coordination on complex tasks.

---

### 5b. ChatDev — Communicative Agents for Software Development

**Citation:**  
Chen Qian, Wei Liu, Hongzhang Liu, Nuo Chen, Yufan Dang, Jiahao Li, Cheng Yang, Weize Chen, Yusheng Su, Xin Cong, Juyuan Xu, Dahai Li, Zhiyuan Liu, and Maosong Sun. "ChatDev: Communicative Agents for Software Development." In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL 2024)*, Volume 1: Long Papers, pp. 15174–15186. Bangkok, Thailand. Association for Computational Linguistics, 2024.

**Links:**  
- arXiv: https://arxiv.org/abs/2307.07924  
- ACL Anthology: https://aclanthology.org/2024.acl-long.810/  
- DOI: https://doi.org/10.18653/v1/2024.acl-long.810

**Verification status:** CONFIRMED. ACL Anthology entry is live and provides the full BibTeX, DOI, and PDF. Authors are from Tsinghua University and affiliated institutions.

**Relevance:** Demonstrates that a "chat chain" of natural-language-communicating LLM agents with defined social roles (analyst, programmer, tester) can autonomously produce working software end-to-end, with a "communicative dehallucination" mechanism to reduce agent errors.

---

## 6. Persistent Memory Architectures for LLM Agents

### 6a. MemGPT — Towards LLMs as Operating Systems

**Citation:**  
Charles Packer, Sarah Wooders, Kevin Lin, Vivian Fang, Shishir G. Patil, Ion Stoica, and Joseph E. Gonzalez. "MemGPT: Towards LLMs as Operating Systems." *arXiv preprint arXiv:2310.08560*, 2023. (Workshop version presented at NeurIPS 2023 workshops; extended version presented at ICML.)

**Links:**  
- arXiv: https://arxiv.org/abs/2310.08560  
- OpenReview: https://openreview.net/forum?id=0Kk142lP62

**Verification status:** CONFIRMED. arXiv ID 2310.08560, submitted 2023-10-12, is live and publicly accessible. All authors are from UC Berkeley. The paper explicitly mentions "Machine Learning, ICML" as the target venue in the document header; a workshop version appeared at NeurIPS 2023. The open-source system was subsequently commercialized as "Letta."

**Relevance:** Proposes an OS-inspired hierarchical memory architecture for LLM agents—distinguishing in-context "main memory" from external "disk" storage and enabling function-call-based paging between tiers—to support unbounded conversation history and document analysis beyond fixed context windows.

---

*End of bibliography. All links were verified as accessible as of the search date (2026-05-15) unless otherwise noted.*
