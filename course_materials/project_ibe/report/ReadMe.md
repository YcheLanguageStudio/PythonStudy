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

**Comparison with PKI**

In traditional Public-Key Infrastructure (PKI), a public-key certificate is required
to bind the key to its user. However, certificates are not required in IBE,
because each user has a unique identity to which they are intrinsically bound.
Instead, IBE requires a trusted central authority called a Private-Key Generator(PKG) for generation and distribution of private keys to registered users.

IBE offers a much simpler solution for many applications, solving the above challenge.
And two reasons are elaborated as follows.

**First Resaon for Simplicity**:

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

**Second Reason for Simplicity**:

Because the decryption key does not need to be generated at
the same time, or by the same entity, as the encryption key, the
trusted third party can delay generating it until the receiving
party has demonstrated its right to have it.

So, there is no need for any party to store keys,
thus, easing the management problem considerably, reducing the risk of inadvertently exposed keys
compromising the secrecy of the protected content.

**Benefits**

Thus, IBE removes several difficulties associated with traditional PKI such
as certificate lookup, lifecycle management, Certificate Revocation Lists and
cross-certification issues giving a greatly-simplified public-key encryption and
signature scheme. Besides, IBE is suitable for the following applications, revocation of public keys, managing user credentials,
delegations of decryption keys, forward secure encryption shcmes.

##Q2
What are the advantages and disadvantages of the IBE over the traditional certificate-based public-key encryption?

##Q3
Can an IBE system be used for signing digital documents? If yes, can the digital signature be used for nonrepudiation?

##Q4
Do you think IBE will be widely used? Please justify your conclusion.
