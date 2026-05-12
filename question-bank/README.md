Round 1 – Infra, Kubernetes, and Cloud Patterns (45 mins)
• Design a multi-tenant EKS cluster with isolation across dev, QA, and prod, with no noisy neighbors.
• What’s your approach to managing 10+ Kustomize overlays without drift or duplication?
• Explain how you’d secure cross-region S3 replication and validate data integrity at scale.
• What happens when systemd hits a failing unit in a containerized node? How would you auto-recover?
• Walk through your strategy to detect & mitigate pod-to-pod lateral movement inside a cluster.
• How do you perform zero-downtime upgrades for a stateful workload using Helm 3?
• Describe a hybrid cloud routing architecture between GCP and AWS. Where do you enforce boundaries?
• Your Terraform state got corrupted during a backend migration. Rebuild strategy?
• Bash One-liner: Find all running containers using more than 500MB RSS memory on a node.

Round 2 – Real Fire, RCA, and Chaos Control (75 mins)
• A new AWS ALB config caused TLS handshakes to fail intermittently. Walk through your full RCA path.
• Kubernetes nodes are healthy. But kubectl logs is blank for critical pods. What’s happening?
• You deployed a sidecar logging agent. Suddenly, CPU throttling spikes. Diagnose and rollback.
• Autoscaling isn’t kicking in despite the CPU crossing the threshold. What’s broken — metrics, HPA, or API server?
• Prod users reporting 504s, but ELB health checks are green. Explain your isolation + triage process.
• Systemd journal logs vanish on reboot across some AMIs. What do you check in the image build and boot sequence?
• A production pod was OOMKilled, but you can’t find logs. Walk through a forensic-level debug.
• Kernel panic on a GKE node mid-deploy. How do you identify if it’s infra, base image, or app-level?

Round 3 – Leadership, Engineering Influence & Production Principles (30 mins)
• How do you design infrastructure that empowers devs without giving them footguns?
• What’s your Linux-level checklist before approving any custom AMI to production?
• You’ve been asked to move from centralized logging to a service-mesh-based observability model. Your tradeoffs?


1. How does DNS resolution work inside a pod?
→ And what do you check when a service isn’t reachable by name?

2. Walk me through what the controller manager does during a Deployment.
→ No rollout status. Reconciliation logic.

3. What happens if a node with local storage gets autoscaled down?
→ Be careful. This one causes data loss in prod more often than you’d think.

4. Post-deploy, latency spikes for 30% of users. No errors. No logs. What now?
→ Your answer reveals if you know how to triage chaos.

5. How do you enforce runtime security in Kubernetes?
→ PSP? AppArmor? OPA? Most people just hope for the best.

6. HPA vs VPA vs Karpenter; when would you NOT use each?
→ Bonus: How would you simulate HPA behavior in staging?

7. Tell me about the last outage you debugged in Kubernetes.
→ No postmortem? You weren’t there.

Week 1 – Core Systems & Linux Mastery
1. Revise Linux internals: systemd, processes, file descriptors, signals.
2. Practice strace, lsof, netstat, tcpdump, debug 3 real scenarios.
3. Daily: Solve 1 bash scripting challenge.
4. Interview Edge: Most fail here. “Pod is healthy, service is green, users see 502.”, Only those who know syscalls + sockets survive.

Week 2 – Kubernetes & Cloud Chaos
1. Re-learn Kubernetes internals: kubelet, controller manager, scheduler, kube-proxy.
2. Practice with KubeSim or minikube chaos: crash DNS, corrupt etcd, simulate node pressure.
3. AWS/GCP: Build multi-region HA VPC.
4. Run a Fault Injection Simulator drill.
5. Interview Edge: Expect: “HPA shows CPU >90%, but no scaling.” 
You’ll be ready to debug metrics pipeline, not YAML.

Week 3 – CI/CD, Infra as Code & Observability
1. CI/CD: Build a pipeline in GitHub Actions + Jenkins.
2. Add rollback + artifact promotion logic.
3. Terraform/Ansible: Create + break infra, recover drift with terraform import & state rm.
4. Observability: Build Prometheus + Grafana dashboards.
5. Trace latency with eBPF or Jaeger.
6. Interview Edge: Be ready for: “Terraform apply failed mid-way” or “Latency doubled with no logs.”

Week 4 – Real Prod Simulation & Story Building
Run 3 outage simulations:
1. Pod OOMKilled, logs missing.
2. DB replication lag 5s under load.
3. Canary passed, but prod is failing.
Write RCA documents using Google/Netflix templates.

Practice answering in STAR format (Situation, Task, Action, Result).
Mock Interview Drill:
Round 1: Linux + Networking.
Round 2: Kubernetes + Cloud Chaos.
Round 3: Leadership + RCA storytelling.
Interview Edge: Senior rounds don’t test YAML. They test if you can stay calm, narrate chaos, and recover with judgment.
The Takeaway: In 30 days, you won’t just “learn tools.” You’ll build scars + stories that make interviewers listen.


Round 1 – Streaming at Scale, K8s, Cloud & Linux (45 mins)
1. How would you design auto-scaling for 50M+ concurrent viewers across multiple K8s clusters without over-provisioning?
2. During an IPL final, a new region needs to spin up instantly. How would you pre-warm nodes & scale workloads with zero cold-start impact?
3. Explain how you’d use Envoy + Istio to route low-latency live streams differently from VOD without service restarts.
4. What’s your approach to multi-zone pod affinity/anti-affinity to ensure a node failure doesn’t impact regional streaming SLAs?
5. How would you monitor HPA scaling decisions in real-time and detect if the metrics server is lagging?
6. Describe K8s readiness/liveness probe configs to catch buffering/lag issues in stream-processing microservices before users notice.
7. A kube-proxy update rolls out mid-match. What’s your network rollback plan to avoid packet drops?

Round 2 – RCA, Fire Drills & Streaming Chaos (75 mins)
1. Playback failures spike for only 3% of users in the APAC region. CPU, memory, and pods look fine. Could you walk through your triage plan?
2. Your Kafka ingestion pipeline lags by 2 minutes during a traffic surge. Producers are fine, consumers are idle. What’s your debug path?
3. Sudden tail latency on Redis-based stream session store during a Champions League match, how do you find & fix the bottleneck?
4. HPA refuses to scale in a critical podset even though Prometheus shows CPU > 90%. Root cause & fix?
5. NAT gateway costs double in 24 hours during a live series; no infra changes were made. What could be silently causing it?

Round 3 – Leadership, Reliability Culture & Scaling Influence (30 mins)
1. How do you build a culture where latency SLOs are enforced like uptime SLAs in a streaming org?
2. You’re asked to ship multi-region failover for live events in 2 weeks with no DNS-based routing allowed. What’s your plan?
3. How would you simulate chaos in a streaming pipeline without risking real user impact?
4. How do you justify infra costs for pre-warmed scaling capacity to executives before a major sports event?

💡 TL;DR:
If you haven’t:
Designed K8s scaling for tens of millions of concurrent sessions
Debugged Kafka lag in real-time ingestion pipelines under pressure
Simulated multi-region failover during live sports events
Root-caused tail latency in caching layers mid-stream
…then a JioHotstar interview will show you exactly where you’re not ready.
But you can train for this chaos.

Round 1 – AI/HPC Scaling, K8s, Cloud & Linux 
1. How would you auto-scale GPU nodes for training workloads without wasting GPU hours on idle pods?
2. A multi-cluster, multi-region AI training job fails halfway because one cluster runs out of GPU memory. How do you rebalance workloads live?
3. How do you configure Kubernetes taints and tolerations for GPU workloads?
4. How would you handle CUDA driver upgrades in K8s without disrupting thousands of running AI pods?
5. Explain how you’d pre-warm GPU nodes for massive AI inference traffic (e.g., ChatGPT-scale) with zero cold-start penalty.
6. How would you monitor GPU utilization in real-time in a Kubernetes cluster?

Round 2 – RCA, Fire Drills & GPU Chaos 
1. How would you check if a GPU pod in Kubernetes is using the GPU assigned to it?
2. What are NCCL logs, and why are they important in distributed training?
3. Persistent storage for AI datasets starts showing 200ms+ latency. How do you pinpoint whether it’s the storage backend, the network, or the GPU node?
4. A Kubernetes GPU pod requests 16GB VRAM but only gets 12GB due to fragmentation. How do you detect and fix in real-time?
5. Your AI pipeline cost doubles in 24 hours with no infra change. Profiling shows a silent GPU resource leak. How do you hunt it down?

Round 3 – Leadership, Reliability Culture & Scaling Influence 
1. How do you set up SLOs for both AI inference latency and batch training completion times without overprovisioning GPUs?
2. You’re told to implement multi-region AI inference failover without DNS-based routing. What’s your plan?
3. How do you justify infra cost for idle GPU pre-warming to leadership when each hour costs $30–$40 per GPU?

TL;DR:
If you haven’t:
Designed GPU-aware K8s schedulers for AI workloads
Debugged NCCL all-reduce failures in distributed training under pressure
Root-caused VRAM fragmentation mid-inference
Balanced batch + real-time AI workloads on the same fleet
…then an NVIDIA interview will show you exactly where your DevOps muscle memory ends.

1. GPU Scheduling (The New Kubernetes Problem)
In AI infra, CPUs don’t matter anymore. GPUs are the bottleneck and they’re brutally expensive.
Real problems teams face:
1. Pods starving GPUs while others sit idle
2. Multi-tenant GPU clusters fighting for memory
3. Batch training vs real-time inference contention
4. MIG, time-slicing, bin-packing gone wrong
If you can design fair, cost-aware GPU scheduling, you’re instantly valuable.

2. Inference Scaling (Not Autoscaling Like You Know It)
Inference traffic is: bursty, unpredictable, latency-sensitive
Scaling here isn’t “HPA + CPU”.
It’s: model warmup delays, cold-start penalties, request batching trade-offs
cache-aware routing, canarying models without killing latency
This is production-grade systems engineering, not YAML tuning.

3. Cost Explosions (The Silent Killer)
One bad model rollout can: double cloud bills overnight, burn GPU credits in hours,make finance panic
AI infra cost problems include: runaway inference calls, over-provisioned GPU nodes, unused embeddings pipelines, zombie feature stores
Engineers who can predict, control, and explain AI infra cost don’t get laid off.
They get promoted.

4. Observability for AI Systems (Where Most Teams Are Blind)
Traditional metrics don’t tell you: why accuracy dropped, why latency spiked only for certain users, why retries exploded downstream, why models drift silently
AI infra observability means:
1. infra + data + model signals together
2. tracing inference paths end-to-end
3. Detecting drift before users complain
This is where DevOps becomes AI systems reliability engineering.

Here’s the uncomfortable truth: AI didn’t kill DevOps. It raised the bar.

Your move 👇
Be honest:
1. Which of these skills do you already have?
2. Which one scares you the most?

Comment GPU, SCALE, COST, or OBSERVABILITY
and repost this so more engineers stop preparing for yesterday’s DevOps roles.

DevOps scenario that quietly breaks strong resumes 👇

Setup:
Two containers running on the same Docker bridge network.

• Container A → Web App
• Container B → API

Web App config: API_URL = http://api:8080

DNS resolves.
Connection establishes.
But requests randomly hang under load.

No errors.
No crashes.
CPU & memory look fine.

Question:
Why does this work sometimes and fail under load?
Where do you debug first?


1. Kubernetes Architecture (The Real Internals)
API Server, etcd, Scheduler, Controller Manager, Kubelet.
Not definitions; how they behave during failures.

2. Pod Lifecycle & Probes
CrashLoopBackOff patterns, liveness vs readiness, startup probes.
Be ready to explain why pods restart, not just how.

3. Scheduler Logic & Node Selection
Taints, tolerations, affinities, and scoring algorithm.
“Why did this pod land on this node?” is a favourite senior question.

4. ReplicaSets, Deployments & Rollout Strategy
Blue-green, canary, rolling updates, surge/unavailable numbers.
Expect a question like: “What happens inside the cluster when you run kubectl apply?”

5. Networking Deep Dive
CNI vs kube-proxy, iptables mode, DNS, MTU issues, packet drops.
If you can’t explain cross-node networking, you’re not getting the offer.

6. Services & Ingress
ClusterIP, NodePort, LoadBalancer, and Ingress controllers.
Be able to map traffic: LB → Ingress → Service → Pod.

7. Resource Requests, Limits & Throttling
CPU throttling, memory OOM, eviction pressure, QoS classes.
Interviewers love asking why apps are slow even when the CPU is 20%.

8. ConfigMaps, Secrets & Environment Management
Not basics; understand how updates propagate, immutability, mounting patterns, and secret decryption.

9. Troubleshooting & Observability
Pod stuck in Pending, ImagePullBackoff, Node NotReady, CNI failures.
Logs + metrics + events + kubelet inspection = senior mindset.

10. StatefulSets, PVCs & Storage Behaviour
PV/PVC binding, ReadWriteOnce issues, storage classes, volume expansion.
If you can explain the failure modes here, you stand out instantly.