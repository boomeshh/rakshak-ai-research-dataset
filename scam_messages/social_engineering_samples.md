# Social Engineering Message Patterns

## Overview

This document provides annotated analysis of social engineering message patterns targeting Indian defence personnel, veterans, and their families. Each pattern documents a distinct scam category observed in the Rakshak AI threat dataset, including the manipulation techniques, urgency triggers, and trust signals employed by threat actors. These samples are entirely synthetic and intended for AI/ML model training, NLP-based threat classification, and cybersecurity awareness research.

---

## Pattern 1: OTP Scam

**Threat Category:** OTP_Scam
**Channel:** SMS

**Sample Message:**
> [OTP VERIFICATION] Your SBI Defence account OTP is 847291. This OTP is valid for 10 minutes. NEVER share this OTP with anyone. If you did not request this, call 1800-XXX-XXXX immediately and visit https://sbionline-defence-salary.net/verify to secure your account.

**Analysis:**
This message employs a classic OTP interception technique. The attacker first sends a fabricated OTP notification to create the illusion of an active session, then exploits the recipient's alarm by suggesting their account may be compromised. The embedded URL is designed to harvest credentials under the guise of "securing" the account. Key manipulation techniques include:
- **False urgency**: The 10-minute validity window pressures the victim to act without thinking.
- **Reverse psychology**: Warning the victim not to share the OTP while simultaneously directing them to a phishing URL creates cognitive dissonance that lowers critical scrutiny.
- **Authority signal**: Use of a toll-free helpline number mimics legitimate bank communications.
- **Fear trigger**: The implication that someone else may have requested the OTP induces panic, overriding rational decision-making.

**Indicators of Compromise:**
- Unsolicited OTP message not preceded by any login attempt by the recipient
- URL domain `sbionline-defence-salary.net` is not an official SBI domain (legitimate domain is `onlinesbi.sbi`)
- Message directs user to a URL to "secure" an account — legitimate banks never do this via SMS
- Hyphenated domain structure (`sbionline-defence-salary`) is a common typosquatting pattern
- Sender ID is generic or numeric rather than an official bank short code

---

## Pattern 2: KYC Fraud

**Threat Category:** KYC_Fraud
**Channel:** WhatsApp

**Sample Message:**
> 🔐 *Defence KYC Compliance — Mandatory Action Required*
> As per the latest RBI circular (Ref: RBI/2024/KYC-DEF-07), all defence salary account holders are required to complete re-KYC by 15 May 2024. Non-compliance will result in a freeze on all transactions including salary credits. Update your KYC now:
> https://kyc-update-defence.in/verify-now
> This is a one-time process. Keep your Aadhaar, PAN, and service number ready.

**Analysis:**
This message impersonates a regulatory directive from the Reserve Bank of India (RBI) to compel defence personnel to submit sensitive identity documents. The fabricated circular reference number (`RBI/2024/KYC-DEF-07`) lends false legitimacy. Manipulation techniques include:
- **Regulatory authority impersonation**: Citing an RBI circular exploits the victim's trust in government institutions and fear of non-compliance penalties.
- **Deadline pressure**: A specific date creates a hard deadline that discourages the victim from verifying the claim through official channels.
- **Financial threat**: The threat of a salary freeze is particularly effective against active defence personnel who depend on timely salary credits.
- **Document harvesting setup**: Requesting Aadhaar, PAN, and service number in a single interaction enables comprehensive identity theft.
- **Reassurance phrase**: "This is a one-time process" reduces perceived risk and encourages compliance.

**Indicators of Compromise:**
- Domain `kyc-update-defence.in` is not affiliated with any official RBI or defence banking portal
- Legitimate RBI KYC notices are communicated through official bank branches and registered email/SMS, not WhatsApp
- The circular reference number format (`RBI/2024/KYC-DEF-07`) does not match official RBI circular numbering conventions
- Request for service number alongside Aadhaar and PAN is atypical for standard KYC processes
- No official government or bank communication requests KYC completion via a WhatsApp link

---

## Pattern 3: Banking Fraud

**Threat Category:** Banking_Fraud
**Channel:** WhatsApp

**Sample Message:**
> 🚨 *URGENT: SBI Defence Account — Suspicious Transaction Detected*
> A transaction of ₹49,800 has been initiated from your SBI Defence Salary Account. If this was NOT authorised by you, click the link below immediately to block the transaction and secure your account:
> https://secure-sbi-defencepay.co.in/auth
> You have 15 minutes to respond before the transaction is processed. Act NOW.

**Analysis:**
This message uses a fabricated transaction alert to trigger immediate panic and bypass rational evaluation. The 15-minute countdown is a high-pressure social engineering technique designed to prevent the victim from calling their bank or verifying the claim independently. Manipulation techniques include:
- **Manufactured crisis**: A specific, large transaction amount (₹49,800) makes the threat feel concrete and personal.
- **Extreme time pressure**: The 15-minute window is deliberately too short for the victim to verify through official channels, forcing reliance on the attacker's link.
- **Action framing**: Framing the phishing link as a "block transaction" tool exploits the victim's protective instinct toward their finances.
- **Capitalised urgency markers**: "URGENT" and "Act NOW" in the message text are designed to activate the fight-or-flight response.
- **Plausible specificity**: The use of a realistic transaction amount and the "SBI Defence Salary Account" label targets a specific demographic with high credibility.

**Indicators of Compromise:**
- Domain `secure-sbi-defencepay.co.in` is not an official SBI domain; legitimate SBI domains use `sbi.co.in` or `onlinesbi.sbi`
- Legitimate banks send transaction alerts via registered SMS with a bank short code, not WhatsApp
- No legitimate bank provides a link to "block" a transaction — customers are directed to call the official helpline
- The `.co.in` TLD combined with hyphenated brand name is a common phishing domain pattern
- Extreme time pressure (15 minutes) is a hallmark of social engineering, not legitimate bank security alerts

---

## Pattern 4: APK Distribution

**Threat Category:** APK_Distribution
**Channel:** Telegram

**Sample Message:**
> 📢 *[OFFICIAL] SPARSH Pension Group — URGENT NOTICE*
> Dear Group Members, the SPARSH Pension Directorate has released a critical security update for the SPARSH mobile app. All pensioners must install the new version immediately to avoid disruption to monthly pension credits. The updated APK has been verified by NIC and is safe to install.
> 👉 Download here: https://sparsh-apk-download.net/SPARSH_Official.apk
> Steps: (1) Uninstall old SPARSH app (2) Download from link above (3) Re-register with your PPO number. For help, reply in this group. — *SPARSH Helpdesk Admin*

**Analysis:**
This message distributes a malicious APK by impersonating the official SPARSH Pension Portal, which is a legitimate Indian government pension management system for defence pensioners. The attacker leverages the high trust placed in SPARSH by veterans and exploits the fear of pension disruption. Manipulation techniques include:
- **Trusted brand impersonation**: SPARSH is a well-known, government-operated system; impersonating it maximises credibility with the target demographic.
- **Third-party verification claim**: Claiming NIC (National Informatics Centre) verification adds a layer of false legitimacy that is difficult for non-technical users to disprove.
- **Pension disruption threat**: The threat of interrupted pension credits is a powerful motivator for elderly veterans on fixed incomes.
- **Step-by-step installation guide**: Providing detailed installation instructions, including enabling "install from unknown sources," normalises a dangerous security bypass.
- **Group authority**: Posting in a Telegram group that appears official creates social proof — if others in the group are complying, the message seems legitimate.

**Indicators of Compromise:**
- Domain `sparsh-apk-download.net` is not the official SPARSH portal (official domain: `sparsh.defencepension.gov.in`)
- The official SPARSH app is distributed exclusively through Google Play Store and Apple App Store, not via direct APK links
- Instructions to uninstall the existing app before installing the new one are designed to remove legitimate security software
- The instruction to enable "install from unknown sources" is a red flag — legitimate apps never require this
- Telegram group names mimicking official government channels are a common APK distribution vector
- `.net` TLD for a government pension portal is atypical; official Indian government portals use `.gov.in`

---

## Pattern 5: Impersonation

**Threat Category:** Impersonation
**Channel:** WhatsApp

**Sample Message:**
> 🪖 *Message from Maj. Gen. A.K. Verma, Army Welfare Directorate, New Delhi*
> Respected Veteran, on behalf of the Chief of Army Staff, I am pleased to inform you that you have been selected for the *Ex-Serviceman Special Housing Assistance Grant 2024* worth ₹1,20,000. This is a one-time benefit under the new welfare policy. Register your claim immediately at:
> https://army-welfare-portaI.org/register
> Slots are limited. Respond within 48 hours. Jai Hind 🇮🇳

**Analysis:**
This message impersonates a senior military officer (Major General rank) to exploit the deeply ingrained respect for hierarchy and authority within the defence community. The fabricated housing grant targets veterans who may be in genuine financial need. Manipulation techniques include:
- **High-rank impersonation**: Invoking a Major General and the Chief of Army Staff creates an authority gradient that discourages questioning or verification.
- **Personalisation signal**: "You have been selected" implies the victim was specifically chosen, triggering a sense of exclusivity and obligation to respond.
- **Large financial incentive**: ₹1,20,000 is a significant sum that motivates action, particularly among veterans on pension incomes.
- **Scarcity trigger**: "Slots are limited" and the 48-hour deadline create artificial urgency that prevents careful verification.
- **Patriotic closing**: "Jai Hind 🇮🇳" is a culturally resonant phrase that reinforces the illusion of official military communication.
- **Formal salutation**: "Respected Veteran" mimics the respectful tone used in genuine military correspondence.

**Indicators of Compromise:**
- Domain `army-welfare-portaI.org` uses a capital letter "I" in place of lowercase "l" in "Portal" — a classic homoglyph typosquatting technique
- Legitimate Army Welfare communications are issued through official channels (registered post, official email, unit notice boards), not WhatsApp
- No legitimate government welfare scheme is communicated via personal WhatsApp messages from senior officers
- The `.org` TLD is atypical for official Indian Army portals (official domains use `.mil.in` or `.gov.in`)
- Requests to "register" on an external portal to claim government benefits are a hallmark of credential harvesting
- Unsolicited messages claiming large financial grants without prior application are a strong indicator of fraud

---

## Pattern 6: Welfare Scheme Fraud

**Threat Category:** Welfare_Scheme_Fraud
**Channel:** SMS

**Sample Message:**
> [SAINIK WELFARE BOARD] Important notice for all veterans: Your Sainik Welfare Board annual benefit of Rs. 15,000 is ready for disbursement. Complete your verification at https://welfare.sparsh-defence.fake-portal.in/login before the deadline of 15 April 2024.

**Analysis:**
This message impersonates the Sainik Welfare Board — a legitimate Indian government body that provides financial assistance to ex-servicemen — to harvest login credentials and personal information. The message is crafted to appear as a routine annual benefit notification. Manipulation techniques include:
- **Legitimate institution impersonation**: The Sainik Welfare Board is a well-known and trusted organisation among veterans; its name immediately establishes credibility.
- **Pre-approved benefit framing**: Stating the benefit is "ready for disbursement" implies the victim has already qualified, removing the need for scepticism about eligibility.
- **Specific monetary amount**: Rs. 15,000 is a plausible annual welfare benefit amount, making the claim believable without being suspiciously large.
- **Deadline pressure**: A specific date (15 April 2024) creates urgency without being as extreme as a 15-minute window, making the message feel more like a routine administrative notice.
- **Verification framing**: Asking for "verification" rather than "login" or "payment details" sounds procedural and low-risk to the victim.
- **SMS channel trust**: SMS is perceived as more official than WhatsApp or Telegram, lending additional credibility to the message.

**Indicators of Compromise:**
- Domain `welfare.sparsh-defence.fake-portal.in` contains the word "fake-portal" — an obvious indicator in this synthetic dataset, but in real attacks, similarly structured domains use plausible-sounding subdomains to obscure the malicious root domain
- Legitimate Sainik Welfare Board communications are issued through district Sainik Welfare Offices, registered post, or official government portals, not SMS links
- The URL structure uses a subdomain (`welfare.sparsh-defence`) on a suspicious root domain (`fake-portal.in`) — a subdomain abuse pattern designed to make the URL appear official at a glance
- No legitimate welfare disbursement requires clicking an SMS link; beneficiaries are contacted through official channels and directed to physical offices or verified government portals
- The combination of a welfare board name with a SPARSH-branded subdomain is inconsistent — these are separate government entities with separate portals
- Absence of a sender ID matching an official government short code is a strong indicator of SMS spoofing
