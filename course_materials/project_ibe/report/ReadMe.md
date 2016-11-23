#Course Project Report: Identity-Based Encrpytion
##Name: CHE Yulin, Student#: 20292673
##Q1
What is the motivation for proposing the identity-based encryption?

**Definition**

Identity-Based Encryption (IBE) is defined as a public-key encryption scheme where any valid string,
which uniquely identifies a user, is the public key of the user.

**Original Motivation**

The original motivation for identity-based cryptography was to simplify certificate management
and thus eliminate the need for Certification Authorities.

**Challenge in Traditional PKI**

With traditional public key cryptography, the generation of the keys,
the publication of the associations between parties and their public keys and
the management of all this require a dedicated secure infrastructure.
Such an infrastructure is expensive, complex, does not scale well to large sizes,
and does not easily extend to manage parties’ attributes, e.g., their roles and rights.

**Comparison with Traditional PKI**

In traditional Public-Key Infrastructure (PKI), a public-key certificate is required
to bind the key to its user. However, certificates are not required in IBE,
because each user has a unique identity to which they are intrinsically bound.
Instead, IBE requires a trusted central authority called a Private-Key Generator(PKG) for generation and distribution of private keys to registered users.

**Simplicity of IBE**

IBE offers a much simpler solution for many applications, solving the above challenge and meeting the orginal motivation.
And two reasons are elaborated as follows.

**First Resaon for Simplicity**

Because the encryption key can be any bit string, it can be chosen by
the encrypting party. The encrypting party can base its choice of bit
string on the needs of the application. First choice is something simple, e.g,
the email address of the receiving party, a digital photograph of the receiving party, a URL.
Second choice is something more complex, e.g, the role of the receiving party, expressed by a list
of attributes he must have, a set of conditions the receiving party must meet,
a policy that the receiving party must conform to, executable program code.

Expressing these requirements in the encryption key relieves the
supporting infrastructure from managing them, thus enabling the
infrastructure to be simpler.

**Second Reason for Simplicity**

Because the decryption key does not need to be generated at
the same time, or by the same entity, as the encryption key, the
trusted third party can delay generating it until the receiving
party has demonstrated its right to have it.

So, there is no need for any party to store keys,
thus, easing the management problem considerably, reducing the risk of inadvertently exposed keys
compromising the secrecy of the protected content.

**Benefit & Application**

Thus, IBE removes several difficulties associated with traditional PKI such
as certificate lookup, lifecycle management, Certificate Revocation Lists and
cross-certification issues giving a greatly-simplified public-key encryption and
signature scheme. Besides, IBE is suitable for the following applications, revocation of public keys, managing user credentials,
delegations of decryption keys, forward secure encryption shcmes.

##Q2
What are the advantages and disadvantages of the IBE over the traditional certificate-based public-key encryption?

There are many disavantages in IBE, while advantages of IBE could be achieved by slightly modifying
traditional certificate-based public-key encryption schema. Thus, disadvantages are elborated first, and
advantages are elaborated second.

###Disadvantages

**PKG PR-Key Compromise Cost Probelm**

We must also trust that the PKG/CA private key is known only to the PKG/CA.
Compromise of the PKG private key compromises the private keys of all users in that
domain. In contrast, compromise of the CA private key enables the attacker to sign and
publish new compromised public keys, tricking senders into encrypting new messages
to these public keys, though it does not compromise existing private keys or messages
encrypted to those keys.

**Revocation of PU-Key Problem**

IBE must use short-lived keys to support revocation, as there is no revocation method for IBE analogous to
X.509’s CRLs or OCSP. So, in practice, the PKG must remain online, with the asso-
ciated increased risk of compromise. Thus, in this aspect, IBE requires stronger trust
assumptions than RSA, requiring a fully-trusted, online entity (the PKG), as opposed to
a partially-trusted (with respect to secrecy of user private keys), offline entity (the CA).

**Users' PR-Key Transmission Problem**

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

**Key Escrow**

It is well understood that IBE includes a type of key escrow, because the PKG
generates the user’s private keys, which causes the following two bad effects,
namely PKG as a possible man-in-the-middle and no non-repudiation guarantee.

**Key Escrow Problem1: PKG as a Possible Man-in-the-Middle**

The PKG is a fully-trusted entity that could
decrypt all messages in the domain, unlike a traditional CA which has no access to user
private keys. IBE provides a weaker form of end-to-end security for encryption than
traditional RSA-based PKIs, with the PKG as a possible man-in-the-middle. Thus, we
can consider IBE trust assumptions to be in between solutions that provide strong end-
to-end security and gateway-based systems, where the sender must trust the recipient’s
domain administrators to properly handle encrypted messages.

**Key Escrow Problem2: No Non-Repudiation Guarantee**

It is well understood that IBE includes a type of key escrow, because the PKG
generates the user’s private keys. PKG is able to sign users' message, thus,
non-repudiation is not guaranteed in IBE. A user could repudiate that the message
is signed by PKG.

##Advantages

**Elimination of User Key Distribution**

In IBE once the sender obtains the parameters of a particular domain’s PKG,
he can compute the public key of any user in that
domain. That is, instead of requiring one online (public) key fetch operation per
recipient as in RSA, IBE only requires one online key fetch operation per domain
(the PKG’s key). By effectively eliminating the need to distribute end user public
keys, IBE addresses a major hurdle in widespread deployment and use of secure
email. This is perhaps the most important benefit of IBE.

**Elimination of Certificate and CA**

Digital certificate and certification authorities are not needed here.
Because receiver’s identifier information is used, sender needn’t to retrieve receiver’s public key.
Thus, CA is not required to issue public keys.

**Policy Based Encryption**

Using IBE the sender can associate arbitrary policies
with the encrypted email message. It can do so by concatenating the policy with the
recipient’s ID prior to computing the public key. When the message is encrypted
using this key, the PKG can enforce the sender’s policy regarding the release of
the private key. For example, the sender can postdate the message by including a
specific date in the encryption key, and the PKG will then release the correspond-
ing key only on or after that date. This benefit is beginning to gain value as email
messaging is being used increasingly for formal communication and is being incor-
porated into workflow systems.

**Implicit client mobility**

In IBE the receiver can contact the PKG whenever it needs
a private key. Therefore, as long as the receiver can contact the PKG, IBE provides
seamless client mobility as the recipient can use any device from any location to
access private keys for email decryption. This benefit is very valuable as users often
check email using a variety of devices such as PDAs and laptops and do so from
a variety of locations. In RSA users can utilize smartcards or online credential
repositories to provide client mobility but this benefit is not provided implicitly.


##Q3
Can an IBE system be used for signing digital documents? If yes, can the digital signature be used for nonrepudiation?

##Q4
Do you think IBE will be widely used? Please justify your conclusion.
