---
title: "About"
showToc: false
hideMeta: true
---

{{< figure src="/img/josh.jpg" alt="Josh Villagomez" class="about-photo" >}}

Hi — I'm **Josh Villagomez**, and *Think Red* is where I think out loud about breaking and defending identity.

I've spent close to 25 years in IT. I came up the way a lot of us did: desktop engineering, TCP/IP, racks of Windows and Linux servers, VMware and Hyper-V, and far too many late nights keeping other people's systems alive. For about a decade I led infrastructure for a 24x7 operation — 300+ servers, thousands of users, a hundred-plus sites — which is a polite way of saying I learned what "high availability" actually costs.

Then the cloud happened, and I followed identity down the rabbit hole. I spent nearly 11 years at **Microsoft**, most recently as a **Senior Partner Technical Advisor for Microsoft Entra**, specializing in hybrid identity and access management. My home turf was the seam between on-prem and cloud: AD DS and Entra ID, directory synchronization with Entra Connect and Cloud Sync, and user and device provisioning — including automated app provisioning to SaaS. Around that core I worked across MFA, Pass-Through Authentication and Password Hash Sync, Single Sign-On, Conditional Access, Windows Hello for Business, and AD FS / Application Proxy. Along the way I mentored and trained hundreds of engineers. If it touches identity, I've probably debugged it at 2 a.m.

## Why red team?

I was a defender for most of my career. Security was baked into everything I built — but the cloud, and now AI, made one thing obvious: defending modern systems is *hard*, and hope is not a control.

A few years ago I volunteered to help a non-profit with their security program, and someone handed me *Red Team Development and Operations* by Joe Vest and James Tubberville. It rearranged how I think. The question that stuck with me: **how do you actually know your controls, processes, and detections work if no one ever tries to break them?** That made too much sense to ignore, so I went deeper into offensive security — not to leave the defender's seat, but to earn it.

That's the whole idea behind *Think Red*: **think like an adversary, write like a defender.** Most of what I publish starts from identity, because that's where I'm strongest and where modern attacks actually land.

## What you'll find here
- Identity-centric red teaming — Entra, AD, and the attack paths in between
- Adversary emulation mapped to [MITRE ATT&CK](https://attack.mitre.org/)
- Red team infrastructure and OPSEC
- AI and LLM red teaming (more on that below)
- Detection and mitigation, always — every offensive post pays its defensive debt

## The AI part

For the last couple of years I've been nose-deep in applied AI. I run local models for experimentation (Ollama, open-weight models like Qwen, orchestrated with Hermes), I've been testing deployments on Microsoft Foundry, and I've grown a little too fond of letting a local reasoning model help me write code at midnight. Lately a lot of that learning has been hands-on with **Claude Code** — building real projects with agentic coding (this site included) and learning the craft by shipping. I've also released AI agents built on **Microsoft Copilot Studio** and **Microsoft 365 Copilot**. Honestly, agent-building has become the part I enjoy most: watching how memory, context, and skills shape the way a model reasons never gets old. I'm convinced the AI solutions that last will be the ones built on solid identity, governance, and secure design — so that's the lens I bring to AI security here.

## How I work
- All research runs in **environments I own or am explicitly authorized to test**.
- Nothing here comes from client or employer engagements unless it's been generalized and cleared.
- Techniques are mapped to ATT&CK and paired with detection and mitigation.

## Away from the keyboard

I live in North Carolina. I play classical piano, travel with my wife whenever we can, and I'm a man of faith who loves to study and teach the Scriptures. I've found the habits that make a decent engineer — curiosity, patience, and a refusal to take systems at face value — tend to make a decent human, too.

A few credentials, for the people who like them: ISC2 **Certified in Cybersecurity (CC)**, and Microsoft **SC-900 / AI-900 / AZ-900**. The fuller résumé lives on [LinkedIn](https://www.linkedin.com/in/jvillago).

## Say hello

Found a problem with this site, or something I published that needs correcting? See [`/.well-known/security.txt`](/.well-known/security.txt) or email **thinkred@jmsg.me**.

- GitHub: [thinkred-dev](https://github.com/thinkred-dev)
- LinkedIn: [jvillago](https://www.linkedin.com/in/jvillago)
- RSS: [/index.xml](/index.xml)

*Views are my own and don't represent any current or former employer. See the [disclaimer](/disclaimer/).*
