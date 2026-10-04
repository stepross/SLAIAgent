"""Rebuild the Play 1-4 setup/takeaway slides on the WebexOne 2026 template."""
import sys

sys.path.insert(0, "/home/ubuntu/work2")
from wxhelpers import *  # noqa: E402,F401,F403

BASE = "/opt/cursor/artifacts/WebexOne2026_GenAI_Webex_Migration.pptx"
OUT = "/opt/cursor/artifacts/WebexOne2026_Play_Updates.pptx"
L_TITLE_ONLY = 6


def setup_slide(prs, play, color, color2, title, files, files_label, prompt, outputs, sanitize, strap, note):
    s = new_slide(prs, L_TITLE_ONLY, title)
    eyebrow(s, f"Play {play} · Setup: data & prompt", color)

    # 1 - data in
    box(s, 0.667, 1.5, 3.75, 4.45, fill=PANEL, radius=0.18)
    circle(s, 0.9, 1.7, 0.5, color, content="1", size=18, color=WHITE, font=HEAD)
    text(s, 1.55, 1.7, 2.8, 0.5, "DATA IN", size=15, color=GREY, font=HEAD, anchor=MSO_ANCHOR.MIDDLE)
    text(s, 0.9, 2.3, 3.4, 0.45, files_label, size=18, font=HEAD, wrap=False)
    two_col = len(files) > 5
    for i, f in enumerate(files):
        if two_col:
            x, y, w = 0.9 + (i % 2) * 1.68, 2.9 + (i // 2) * 0.58, 1.6
        else:
            x, y, w = 0.9, 2.9 + i * 0.68, 3.3
        size = 13 if two_col or max(len(n) for n in files) > 22 else 14
        box(s, x, y, w, 0.48, fill=WHITE, line=LINE, radius=0.1, content=f, size=size,
            font=BODY if two_col else MONO, color=DARK, wrap=False, margins=(0.04, 0, 0.04, 0))

    arrow(s, 4.47, 3.72, 4.82, 3.72, color=GREY, width=2.5)

    # 2 - master prompt
    box(s, 4.87, 1.5, 4.55, 4.45, fill=INK, radius=0.18)
    circle(s, 5.1, 1.7, 0.5, color, content="2", size=18, color=WHITE, font=HEAD)
    text(s, 5.75, 1.7, 3.5, 0.5, "MASTER PROMPT", size=15, color=MID, font=HEAD, anchor=MSO_ANCHOR.MIDDLE)
    text(s, 5.1, 2.4, 4.2, 3.4, [[(k.ljust(8), {"color": SKY}), (v, {"color": WHITE})] for k, v in prompt],
         size=13, font=MONO, space_after=9, wrap=False)

    arrow(s, 9.47, 3.72, 9.82, 3.72, color=GREY, width=2.5)

    # 3 - output
    box(s, 9.87, 1.5, 2.8, 4.45, fill=grad(color, color2, 45), radius=0.18)
    circle(s, 10.1, 1.7, 0.5, WHITE, content=[[("3", {"color": color})]], size=18, font=HEAD)
    text(s, 10.75, 1.7, 1.8, 0.5, "OUTPUT", size=15, color=WHITE, font=HEAD, anchor=MSO_ANCHOR.MIDDLE)
    for i, (ic, lbl) in enumerate(outputs):
        y = 2.45 + i * 1.12
        icon(s, ic, 10.1, y, 0.5, WHITE)
        text(s, 10.75, y - 0.1, 1.85, 0.95, lbl, size=16, color=WHITE, font=HEAD, spacing=0.95)

    # sanitize + strap
    box(s, 0.667, 6.12, 5.6, 0.62, fill=WHITE, line=PINK, line_width=1.5, radius=0.31)
    icon(s, "privacy", 0.85, 6.2, 0.46, PINK)
    text(s, 1.45, 6.12, 4.75, 0.62, [[("Sanitize  ", {"color": PINK}), (sanitize, {"color": DARK})]],
         size=15, font=HEAD, anchor=MSO_ANCHOR.MIDDLE, wrap=False)
    box(s, 6.47, 6.12, 6.2, 0.62, fill=INK, radius=0.31, content=strap, size=16, color=WHITE, font=HEAD,
        wrap=False, margins=(0.05, 0, 0.05, 0))
    notes(s, note)
    return s


def takeaway_slide(prs, play, color, color2, title, purged, built, stats, key, note):
    s = new_slide(prs, L_TITLE_ONLY, title)
    eyebrow(s, f"Play {play} · What we learned", color)

    # purged
    box(s, 0.667, 1.5, 3.7, 4.5, fill=PANEL, radius=0.18)
    text(s, 0.95, 1.68, 3.2, 0.4, "PURGED", size=15, color=GREY, font=HEAD)
    for i, p in enumerate(purged):
        y = 2.2 + i * 1.22
        box(s, 0.95, y, 3.15, 1.0, fill=WHITE, line=LINE, radius=0.12)
        circle(s, 1.08, y + 0.32, 0.36, MID, content="\u2715", size=12, color=WHITE, font=HEAD)
        text(s, 1.58, y, 2.45, 1.0, [[(p, {"strike": True})]], size=16, color=GREY, font=HEAD,
             anchor=MSO_ANCHOR.MIDDLE, spacing=0.95)

    box(s, 4.47, 3.3, 0.55, 0.85, fill=grad(color, color2, 0), shape=MSO_SHAPE.RIGHT_ARROW, radius=None)

    # built
    box(s, 5.12, 1.5, 4.0, 4.5, fill=grad(color, color2, 45), radius=0.18)
    text(s, 5.4, 1.68, 3.5, 0.4, "BUILT ON WEBEX", size=15, color=WHITE, font=HEAD)
    for i, (ic, head, sub) in enumerate(built):
        y = 2.2 + i * 1.22
        box(s, 5.4, y, 3.45, 1.0, fill=WHITE, radius=0.12)
        icon(s, ic, 5.55, y + 0.25, 0.5, color)
        text(s, 6.2, y + 0.1, 2.6, 0.45, head, size=17, font=HEAD, wrap=False)
        text(s, 6.2, y + 0.5, 2.6, 0.45, sub, size=13, color=GREY, spacing=0.95)

    # impact
    text(s, 9.4, 1.55, 3.2, 0.4, "IMPACT", size=15, color=GREY, font=HEAD)
    for i, (num, lbl) in enumerate(stats):
        y = 2.0 + i * 1.35
        text(s, 9.4, y, 3.27, 0.75, num, size=40, color=color, font=HEAD, wrap=False)
        text(s, 9.4, y + 0.72, 3.27, 0.5, lbl, size=15, color=DARK, font=HEAD)

    box(s, 0.667, 6.15, 12.0, 0.62, fill=INK, radius=0.31,
        content=[[("Takeaway:  ", {"color": SKY}), (key, {"color": WHITE})]], size=18, font=HEAD,
        wrap=False, margins=(0.05, 0, 0.05, 0))
    notes(s, note)
    return s


def build():
    prs = Presentation(BASE)
    sld_ids = prs.slides._sldIdLst
    for sld_id in list(sld_ids):
        prs.part.drop_rel(sld_id.rId)
        sld_ids.remove(sld_id)

    # ---------------- Play 1 - UCCX
    setup_slide(
        prs, 1, BLUE, PINK, "Scripts + reports in. Build recipe out.",
        ["script.aef / XML", "csq_activity.csv", "wrapup_reasons.csv", "ivr_traffic.csv"],
        "Script + 3 CUIC 15 reports",
        [("ROLE", "Principal WxCC architect"),
         ("MANDATE", "No 1:1 DTMF ports"),
         ("FIND", "50%+ self-service deflection"),
         ("", "45-60s less wrap-up per call"),
         ("STACK", "AI Agent · AI Assistant"),
         ("", "Flow Designer · skill queues"),
         ("OUTPUT", "Node-by-node recipe"),
         ("", "No brittle JSON ASTs")],
        [("graph", "Flow Designer recipe"), ("cc_ai", "AI Agent system prompts"),
         ("analytics", "Deflection targets")],
        "PII, account #s, DB passwords",
        "Raw .aef + CUIC CSVs \u2192 50%+ AI deflection",
        """
SLIDE SETUP: PLAY 1 DEMO (UCCX TO WEBEX CONTACT CENTER) - THE DATA & THE PROMPT
TALK TRACK (1 MINUTE):
"Before we roll the video playback for Demo 1, let's look at how we set this up.
First, gathering the data: You don't need access to raw database backends. In UCCX, we export the application script (.aef) from the script repository or print the script XML, and we pull three standard CUIC 15 reports: CSQ queue activity, agent wrap-up reasons, and IVR traffic drop-off data. We sanitize any customer PII.
Second, the Master Prompt: We instruct the LLM acting as a Principal Cisco Solutions Architect with a strict mandate: 'Don't Just Migrate, Transform.' We command it not to output raw JSON ASTs that fail tenant imports, but to deliver a click-by-click Flow Designer Programming Recipe, uncover high-volume deflection opportunities with Webex AI Agent, and automate post-call work with Webex AI Assistant.
Let's watch the recorded execution in action."

DETAIL (from original slide):
- Source: UCCX Script Editor / Script Repository (.aef Java-serialized binary or printed XML).
- CUIC 15 reports: CSQ Activity Summary (csq_activity.csv), Agent Wrap-Up Summary (wrapup_reasons.csv), IVR Traffic Analysis (ivr_traffic.csv).
- Extraction captures operating schedules, REST API CRM lookups, DTMF option branches, CSQ queue targets, and Set Enterprise CAD variables.
- Sanitization gate: replace customer PII, account numbers and internal database passwords with synthetic tokens.
- Prompt persona: Principal Cisco Enterprise Contact Center Solutions Architect (UCCX to WxCC). Forbids 1:1 DTMF porting; mandates 50%+ self-service deflection and 45-60s agent ACW reduction. Native stack only: Webex AI Agent, Webex AI Assistant, Flow Designer, skill-based queues - zero third-party engines. Deliverable: node-by-node Flow Designer build instructions + ready-to-paste AI Agent system prompts.
""")
    takeaway_slide(
        prs, 1, BLUE, PINK, "UCCX: not a port. A transformation.",
        ["4-level touch-tone tree", "Hard-coded Java REST steps", "45-60s manual wrap-up"],
        [("cc_ai", "Webex AI Agent", "Loans · rates · resets + SMS"),
         ("headset", "Webex AI Assistant", "Screen pop · sentiment · GenAI wrap-up"),
         ("graph", "8-node Flow recipe", "Drag-and-drop in Control Hub")],
        [("52%", "tier-1 calls deflected"), ("150+ hrs", "agent time back / month"),
         ("80%", "faster design: weeks \u2192 minutes")],
        "Moving to WxCC is an AI-first transformation, not script porting.",
        """
SLIDE TAKEAWAYS: PLAY 1 (UCCX TRANSFORMATION) - WHAT WE LEARNED
TALK TRACK (1 MINUTE):
"Here are the key takeaways from Play 1:
1. Technical Debt Purged: We completely eliminated the legacy touch-tone maze. No customer should have to navigate 4 levels of phone menus in 2026.
2. Target Webex Architecture: We achieved true AI-first modernization. By deploying Webex AI Agent at the front door, we deflect 52% of transactional volume, while Webex AI Assistant equips agents with real-time context and eliminates after-call work.
3. Quantifiable ROI: The business case is compelling - thousands of dollars saved in agent wrap-up time and an 80% reduction in professional services delivery time.
Now, let's move to Play 2 and see how we apply this exact same methodology to CUCM Hunt Pilots."

DETAIL (from original slide):
- Purged: 4 levels of nested DTMF menus ('Press 1 for Mortgage, Press 2 for Rates...') that drove caller drop-offs; hard-coded Java REST steps and XML exception handlers (replaced by native HTTP Request nodes); 45-60 seconds of manual post-call wrap-up per call.
- Built: Webex AI Agent natural-language voice self-service for Loan Status, Rate Quotes and Password Resets with automated SMS link dispatch; Webex AI Assistant with screen-pop context, conversational sentiment and GenAI wrap-up summaries; a turnkey 8-node Flow Designer blueprint.
- Impact: 52% tier-1 call deflection; 45-60s saved per call (150+ agent hours/month); assessment and flow design reduced from 3 weeks to minutes (80% faster).
""")

    # ---------------- Play 2 - Hunt Pilots
    setup_slide(
        prs, 2, CYAN, BLUE, "Graph every hunt chain",
        ["hunt_pilots.csv", "hunt_lists.csv", "line_groups.csv", "phones_lines.csv"],
        "4 CUCM BAT exports",
        [("ROLE", "Principal UC architect"),
         ("GRAPH", "Pilot \u2192 list \u2192 group \u2192 phone"),
         ("DETECT", "Circular RNA loops"),
         ("", "Orphaned line groups"),
         ("TIER", "Customer Assist"),
         ("", "Auto Attendant"),
         ("", "Hunt Group · direct DN")],
        [("graph", "Dependency graph"), ("search_person", "Loop + orphan report"),
         ("people", "Right-sized queue map")],
        "Extensions, MACs (per policy)",
        "100+ hunt chains graphed. Zero spreadsheets.",
        """
SLIDE SETUP: PLAY 2 DEMO (HUNT PILOTS TO CUSTOMER ASSIST) - THE DATA & THE PROMPT
TALK TRACK (1 MINUTE):
"In Play 2, we tackle on-premises CUCM Hunt Pilots. Over 10 to 15 years, every enterprise accumulates dozens of hunt pilots, circular overflow loops, and abandoned line groups.
Data Gathering: We use standard CUCM Bulk Administration Tool (BAT) CSV exports: Hunt Pilots, Hunt Lists, Line Groups, and Phone Line associations.
Master Prompt: We task the LLM to graph the entire dependency matrix. The prompt explicitly commands the model to find circular RNA loops that drop calls, flag orphaned groups, and right-size each queue into Webex Calling tiers - elevating high-touch departmental queues to Webex Calling Customer Assist with AI wrap-up, while retaining simple hunt groups for basic coverage.
Let's watch the recorded demonstration."

DETAIL (from original slide):
- Source: CUCM Administration > Bulk Administration > Hunt Pilots / Hunt Lists / Line Groups / Phones > Export.
- Files: cucm_bat_hunt_pilots.csv, cucm_bat_hunt_lists.csv, cucm_bat_line_groups.csv, cucm_bat_phones_lines.csv.
- Captures distribution algorithms (Top-Down, Circular, Longest-Idle), RNA timers, pilot numbers and agent line memberships.
- Sanitization gate: mask internal extensions and device MAC addresses if customer policy requires.
- Prompt persona: Principal Cisco UC & Routing Solutions Architect (CUCM queue rationalization). Reconstruct the dependency tree from Hunt Pilot down to physical endpoints; detect circular RNA loops (e.g., 8801 <-> 8802) and orphaned line groups with zero registered devices; categorize into Customer Assist vs. Auto Attendant vs. native Hunt Group vs. direct extension.
""")
    takeaway_slide(
        prs, 2, CYAN, BLUE, "Clean before you move",
        ["2 orphaned hunt pilots", "RNA loop 8801 \u21c4 8802", "15 CUCM tables of sprawl"],
        [("headset", "Customer Assist", "IT Helpdesk 4100 · Billing 5200"),
         ("people", "Agent screen pops", "Caller, dialed number, reason"),
         ("phone", "Simple Hunt Group", "Facilities 3000 stays basic")],
        [("0", "garbage configs migrated"), ("Live", "queue depth, agent state, SLA"),
         ("5 min", "topology audit vs. weeks")],
        "GenAI rationalizes hunt chains, so you migrate only what adds value.",
        """
SLIDE TAKEAWAYS: PLAY 2 (HUNT PILOT RATIONALIZATION) - WHAT WE LEARNED
TALK TRACK (1 MINUTE):
"Key takeaways from Play 2:
1. Clean Before You Move: Never migrate legacy configurations 1-to-1 without auditing them first. GenAI found circular RNA loops and ghost queues that had been lurking in CUCM for years.
2. Right-Size to Webex Customer Assist: Not every queue needs a full contact center license, but high-touch teams like IT and Billing deserve more than a dumb desk-phone ring. Customer Assist bridges that gap perfectly with agent screen pops and supervisor analytics.
3. Operational Clarity: We simplified decades of on-prem complexity into a clean, modern Control Hub setup.
Next, let's look at Play 3: Modernizing Cisco Unity Connection with Webex 24/7 AI Receptionist."

DETAIL (from original slide):
- Purged: 2 deprecated hunt pilots pointing to empty line groups with zero registered devices; infinite ring cycles (8801 <-> 8802) that dropped calls; 15 multi-tier CUCM tables consolidated into a single-pane Control Hub model.
- Built: Customer Assist for high-impact teams (IT Helpdesk 4100, Billing 5200) with supervisor analytics; screen pops with caller profile, dialed number and reason for call; lightweight broadcast Hunt Group retained for Facilities 3000.
- Impact: only active, rationalized logic migrated; real-time queue depth, agent state and SLA metrics for team leads; weeks of spreadsheet mapping reduced to a 5-minute automated topology audit.
""")

    # ---------------- Play 3 - Unity
    setup_slide(
        prs, 3, PINK, VIOLET, "Turn greetings into a knowledge base",
        ["cuc_call_handlers.csv", "cuc_menu_entries.csv", "cuc_greetings_transcripts.csv",
         "cuc_company_directory.csv"],
        "CallHandlerDataDump",
        [("ROLE", "Principal collab architect"),
         ("FLATTEN", "3-tier DTMF \u2192 speech"),
         ("", "Request \u2192 destination"),
         ("CONVERT", "45s greetings \u2192 FAQ"),
         ("ACTION", "SMS links to callers"),
         ("TARGET", "Webex AI Receptionist")],
        [("chat", "AI Receptionist FAQ table"), ("graph", "Intent \u2192 destination map"),
         ("phone", "SMS follow-up actions")],
        "Staff cell #s \u2192 company DIDs",
        "Static audio \u2192 24/7 conversational Q&A",
        """
SLIDE SETUP: PLAY 3 DEMO (UNITY CONNECTION TO AI RECEPTIONIST) - THE DATA & THE PROMPT
TALK TRACK (1 MINUTE):
"In Play 3, we address Cisco Unity Connection. For 20 years, companies have forced callers to listen to 45-second recorded greetings: 'For office hours press 1, for directions press 2, for billing press 3...'
Data Gathering: We run the standard CallHandlerDataDump utility from Cisco Unity Tools to export call handler tables, DTMF menu entries, and transcribed greeting audio.
Master Prompt: We prompt the LLM to deconstruct the multi-level tree, convert static audio monologues into a structured FAQ Knowledge Base for Webex 24/7 AI Receptionist, and configure dynamic SMS link dispatch.
Let's watch the recorded walkthrough."

DETAIL (from original slide):
- Source utility: Cisco Unity Tools CallHandlerDataDump.exe (or CSV export via CUC Administration / REST API).
- Files: cuc_call_handlers.csv (handlers & schedules), cuc_menu_entries.csv (DTMF keys 0-9), cuc_greetings_transcripts.csv (greeting audio as text), cuc_company_directory.csv.
- Greeting audio transcribed to text across standard, closed, holiday and informational handlers.
- Sanitization gate: replace employee cell-phone transfer numbers with internal company DIDs.
- Prompt persona: Principal Cisco Collaboration Solutions Architect (Unity Connection voice modernization). Flatten 3-tier touch-tone menus and map spoken requests directly to destinations; convert static 45-second recordings (hours, directions, invoicing) into a ready-to-paste AI Receptionist FAQ table; configure automated SMS links (directions, portals) to caller mobiles.
""")
    takeaway_slide(
        prs, 3, PINK, VIOLET, "Make the front door a conversation",
        ["45-second menu monologues", "3-tier IVR maze", "After-hours voicemail dead ends"],
        [("mic", "24/7 AI Receptionist", "Greets, answers, routes"),
         ("chat", "SMS follow-up", "Directions · parking · payments"),
         ("headset", "Smart escalation", "Customer Assist + screen pop")],
        [("1 turn", "to the right destination"), ("24/7", "answers, zero hold time"),
         ("Staff", "freed from repetitive calls")],
        "Stop making callers listen. Let them talk.",
        """
SLIDE TAKEAWAYS: PLAY 3 (UNITY MODERNIZATION) - WHAT WE LEARNED
TALK TRACK (1 MINUTE):
"Key takeaways from Play 3:
1. Stop Forcing Callers to Listen to Menus: Webex 24/7 AI Receptionist turns rigid on-prem voicemail trees into an intelligent, conversational front door.
2. Multimodal Self-Service: By combining conversational voice answering with automated SMS link dispatch, callers get immediate resolution on their mobile devices.
3. Elevated Routing: Staff are protected from routine interruptions, while high-value calls reach the right department instantly.
Now let's examine our fourth and final play: CUCM Dial Plan & Local Gateway (CUBE) Hybrid Coexistence."

DETAIL (from original slide):
- Purged: 45-second static recordings listing menu options; nested 3-tier call handlers flattened into a single-turn conversational front door; unmonitored after-hours voicemail boxes replaced with 24/7 conversational FAQ self-service.
- Built: 24/7 AI Receptionist that greets callers, answers from the knowledge base and routes dynamically; instant SMS links for directions, parking and payment portals; escalation of complex inquiries to Webex Calling Customer Assist with screen-pop context.
- Impact: immediate answers to routine questions 24/7 with no hold; callers speak naturally instead of hunting for dial-pad keys; receptionists freed from repetitive directions/scheduling questions.
- Original key takeaway: "Stop forcing callers to listen to 45 seconds of options. Webex 24/7 AI Receptionist turns the front door into a conversational asset."
""")

    # ---------------- Play 4 - Dial plan / LGW
    setup_slide(
        prs, 4, ORANGE, PINK, "Dial plan in. CUBE config out.",
        ["routepattern", "translationpattern", "gateway", "trunk", "routegroup", "routelist", "partition",
         "css", "phone", "ctiroutepoint"],
        "10 CUCM BAT CSVs",
        [("ROLE", "Principal routing architect"),
         ("AUDIT", "Legacy H.323 gateways"),
         ("", "Old prefixes 91.10D, 9.01"),
         ("NORMAL", "+E.164 hybrid matrix"),
         ("", "on-prem \u21c4 cloud users"),
         ("CLI", "IOS-XE CUBE config"),
         ("", "syntax-validated")],
        [("download", "CUBE dial-peers + SIP profiles"), ("phone", "+E.164 routing matrix"),
         ("search_person", "Tech-debt audit")],
        "Carrier IPs, trunk passwords",
        "Production-ready CUBE CLI. Zero downtime.",
        """
SLIDE SETUP: PLAY 4 DEMO (DIAL PLAN & LOCAL GATEWAY) - THE DATA & THE PROMPT
TALK TRACK (1 MINUTE):
"In Play 4, we tackle the biggest migration hurdle: enterprise dial plans and hybrid PSTN routing.
Data Gathering: We export 10 core CUCM BAT CSV files covering Route Patterns, Translation Patterns, Gateways, Trunks, Route Groups, and Partitions.
Master Prompt: We prompt the LLM to audit legacy technical debt - such as flagging obsolete H.323 gateways that cannot connect to the cloud - normalize all extensions to enterprise +E.164, and generate production-ready Cisco IOS-XE CUBE CLI configurations for zero-downtime hybrid coexistence.
Let's watch the recorded demonstration."

DETAIL (from original slide):
- Source: CUCM Administration > Bulk Administration > Route Plan / Call Routing / Gateways / Trunks > Export.
- Files: routepattern.csv, translationpattern.csv, gateway.csv, trunk.csv, routegroup.csv, routelist.csv, partition.csv, css.csv, phone.csv, ctiroutepoint.csv.
- Extracts on-prem routing chains, legacy H.323/MGCP gateways, translation patterns and CSS/partition permissions.
- Sanitization gate: replace public carrier IP addresses and trunk authentication passwords with synthetic values.
- Prompt persona: Principal Cisco Enterprise Collaboration & Routing Solutions Architect (CUCM to Webex Local Gateway). Identify legacy H.323 gateways (e.g., 198.18.128.11) and strip obsolete steering prefixes (91.10D, 9.01); build a bidirectional +E.164 hybrid routing matrix (+197255560XX <-> +197255570XX) for phased migration; generate complete IOS-XE CUBE blocks (voice service voip, translation-rules, dial-peers, sip-profiles).
""")
    takeaway_slide(
        prs, 4, ORANGE, PINK, "Hybrid coexistence: migrate at your pace",
        ["H.323 / MGCP gateways", "Steering prefixes 91.10D, 9.", "Hundreds of CSS / partitions"],
        [("integration", "CUBE Local Gateway", "Generated CLI · TLS / SRTP"),
         ("phone", "Hybrid dialing", "+197255560XX \u21c4 +197255570XX"),
         ("transcript", "Voicemail AI", "Transcripts to email + Webex App")],
        [("0", "downtime, dept-by-dept"), ("1", "shared PSTN trunk"),
         ("Minutes", "not weeks of dial-peers")],
        "Migrate thousands of users at your own pace, without disruption.",
        """
SLIDE TAKEAWAYS: PLAY 4 (DIAL PLAN & HYBRID COEXISTENCE) - WHAT WE LEARNED
TALK TRACK (1 MINUTE):
"Key takeaways from Play 4:
1. Risk-Free Phased Migration: Hybrid routing is the linchpin of enterprise migrations. By generating accurate CUBE Local Gateway configs, we give customers the freedom to migrate users at their own pace without changing extension numbers or disrupting carrier PSTN contracts.
2. Modernization Beyond Routing: We don't just migrate dial peers - we modernize voicemail into AI-driven speech-to-text transcription delivered straight to Webex App.
3. Engineering Velocity: What used to require weeks of manual dial-peer scripting and testing is delivered in minutes with zero-code GenAI precision.
Now, let's move into Section 3: Trust, Guardrails, and Human-in-the-Loop Verification."

DETAIL (from original slide):
- Purged: legacy H.323 and MGCP gateways incompatible with cloud signaling; redundant steering prefixes (91.10D, 9.) replaced by standardized +E.164 patterns; hundreds of legacy CSS permissions rationalized into unified Control Hub routing policies.
- Built: auto-generated, syntax-validated IOS-XE CUBE Local Gateway dial-peers connecting CUCM to Webex Calling over TLS/SRTP; bidirectional extension dialing between on-prem (+197255560XX) and cloud (+197255570XX) users; location-wide Voicemail AI Transcription with email and Webex App delivery.
- Impact: department-by-department migration with zero disruption; one carrier trunk shared by on-prem and cloud users during transition; AI voicemail transcripts instead of audio inbox lag.
""")

    prs.save(OUT)
    print("saved", OUT, len(prs.slides))


if __name__ == "__main__":
    build()
