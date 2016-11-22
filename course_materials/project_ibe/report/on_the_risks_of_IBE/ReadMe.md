#On the Risks of IBE
##Q2
What are the advantages and disadvantages of the IBE over the traditional certificate-based public-key encryption?

**Disadvantages**

In choosing any security system, we must recognize and accept the associated trust as-
sumptions. How do the trust assumptions of IBE differ from those we have come to
accept for RSA-based PKIs? In both systems, we place trust in the correctness of the
cryptographic algorithms and their implementations. We must also place trust in the
management of cryptographic keys: how the sender determines the correct public key
for a recipient and how the recipient’s private key(s) are secured, so both parties have
confidence that the communication is private. As IBE provides a novel key distribu-
tion mechanism, we should closely examine the trust assumptions associated with that
mechanism.As described previously, we believe that practical deployment of IBE and/or RSA
requires domain-based administration of keying material, where each domain manages
its own PKG or CA. In either case, the sender must obtain the PKG public key/paramet-
ers or the CA certificate for the recipient’s domain in a trustworthy manner to allow the
sender to determine the public key of the recipient. For IBE, this enables the sender
to compute the public key. For RSA, this enables the sender to lookup the recipient’s
certificate in a directory [12], [13], and by verifying the CA’s signature on the certifi-
cate, obtain the recipient’s public key. In this aspect, IBE and RSA have similar trust
assumptions. In practice, PKG parameters and CA certificates can both be distributed
via DNS/DNSSEC [1], [8], [16].

We must also trust that the PKG/CA private key is known only to the PKG/CA.
Compromise of the PKG private key compromises the private keys of all users in that
domain. In contrast, compromise of the CA private key enables the attacker to sign and
publish new compromised public keys, tricking senders into encrypting new messages
to these public keys, though it does not compromise existing private keys or messages
encrypted to those keys. In RSA-based PKIs, this risk is typically addressed by keep-
ing the CA private key offline so it is not subject to online attacks. Keeping the PKG
offline is feasible only if long-lived keys are used. However, IBE must use short-lived
keys to support revocation [4], as there is no revocation method for IBE analogous to
X.509’s CRLs or OCSP. So, in practice, the PKG must remain online, with the asso-
ciated increased risk of compromise. Thus, in this aspect, IBE requires stronger trust
assumptions than RSA, requiring a fully-trusted, online entity (the PKG), as opposed to
a partially-trusted (with respect to secrecy of user private keys), offline entity (the CA).
We also require a trustworthy process by which recipients obtain and manage their
private keys. For modern RSA PKIs, recipients typically generate and maintain sole
control over their private keys. As part of the certificate request and issuance process,
the CA requires the keyholder to authenticate and prove posession of the private key,
typically by signing the certificate request. For IBE, the PKG generates the private key
and sends it to the recipient via a private, authenticated channel. Thus, in both cases, we
must trust the user authentication to the PKG or CA, so private keys are not associated
with the wrong recipients. For IBE, however, we must also trust that the private key
is not compromised at the PKG or on the network. Again, IBE requires stronger trust
assumptions than RSA.

It is well understood that IBE includes a type of key escrow, because the PKG
generates the user’s private keys [2], [5]. The PKG is a fully-trusted entity that could
decrypt all messages in the domain, unlike a traditional CA which has no access to user
private keys. IBE provides a weaker form of end-to-end security for encryption than
traditional RSA-based PKIs, with the PKG as a possible man-in-the-middle. Thus, we
can consider IBE trust assumptions to be in between solutions that provide strong end-
to-end security and gateway-based systems, where the sender must trust the recipient’s
domain administrators to properly handle encrypted messages [3], [7].

Thus, we conclude that, to solve the key distribution problem for secure email, IBE
requires us to accept stronger trust assumptions, when compared with RSA-based PKIs.
The IBE PKG is a fully-trusted entity which must remain online in practice to support
the use of short-lived keys for revocation. Unlike an offline CA,
the PKG can decrypt allmessages destined for recipients in the domain,
providing a weaker form of end-to-end security than traditional RSA-based PKIs.


**Advantages**

We identify three unique benefits of IBE that are not provided by today’s RSA based
secure email systems such as S/MIME.

1. Eliminate user key distribution. In IBE once the sender obtains the parameters
of a particular domain’s PKG, he can compute the public key of any user in that
domain. That is, instead of requiring one online (public) key fetch operation per
recipient as in RSA, IBE only requires one online key fetch operation per domain
(the PKG’s key). By effectively eliminating the need to distribute end user public
keys, IBE addresses a major hurdle in widespread deployment and use of secure
email. This is perhaps the most important benefit of IBE.

2. Policy based encryption. Using IBE the sender can associate arbitrary policies
with the encrypted email message. It can do so by concatenating the policy with the
recipient’s ID prior to computing the public key. When the message is encrypted
using this key, the PKG can enforce the sender’s policy regarding the release of
the private key. For example, the sender can postdate the message by including a
specific date in the encryption key, and the PKG will then release the correspond-
ing key only on or after that date. This benefit is beginning to gain value as email
messaging is being used increasingly for formal communication and is being incor-
porated into workflow systems. For example, in secure role based messaging for
healthcare [14] a patient can compose a message to “cardiologist on duty”. How-
ever, in such applications the policy itself might be sensitive; e.g., this example
policy could indicate that the patient has a heart problem. In IBE, this policy is
accessible in the cleartext as the message travels from the sender to the recipient.

3. Implicit client mobility. In IBE the receiver can contact the PKG whenever it needs
a private key. Therefore, as long as the receiver can contact the PKG, IBE provides
seamless client mobility as the recipient can use any device from any location to
access private keys for email decryption. This benefit is very valuable as users often
check email using a variety of devices such as PDAs and laptops and do so from
a variety of locations. In RSA users can utilize smartcards or online credential
repositories to provide client mobility but this benefit is not provided implicitly.

**conclusion**

We began this study with two questions in mind. First, what are the benefits of using an
IBE system for the critical application of world-wide secure email as well the necessary
assumptions in achieving these benefits? Second, can these same benefits be achieved
(without increased assumptions) with conventional mechanisms such as RSA?

In answering the first question we have identified three unique benefits of IBE,
namely, reducing the key distribution requirement from once per recipient to once
per domain, providing policy based encryption, and providing implicit client mobility.
However, these benefits have significant costs associated with them. First, they come
with weaker notions of end-to-end security where an entity besides the recipient (the
PKG) has the necessary secrets for decrypting messages. Second, the PKG is a fully
trusted entity representing a single point of trust failure whereby its compromise al-
lows an adversary to compute the private keys of all the users of that domain. Third,
this fully trusted entity is always online and thereby vulnerable to attacks. Interestingly,
these same negatives have been carefully weighed over time by the research commu-
nity resulting in norms that require strong notions of end-to-end security, CAs that onlysign public keys but do not generate user private keys, and CAs that remain largely of-
fline. Therefore, we argue that considerable thought must be given to these costs before
adopting IBE.

In answering the second question we propose a simple solution that achieves all the
benefits of IBE. Table 1 compares the solution with existing systems. Our solution uses
simpler and widely-understood RSA mechanisms. Furthermore, the solution ensures
privacy of the policy in policy-based-encryption where the policy itself might be sensi-
tive. Therefore, we argue that even if one is willing to incur the costs associated with
identity based encryption, simpler alternatives to IBE are available. As an example one
could easily design a secure role based messaging system with IB-MKD that satisfies
the requirements identified by Mont et al. [14].
