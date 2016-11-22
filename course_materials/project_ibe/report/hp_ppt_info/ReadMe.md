#HP-Invent
##Q1
What is the motivation for proposing the identity-based encryption?

**Encryption**:

Encryption schemes solve the problem of keeping data secret from undesired viewers,
but create a problem of managing the keys.

**Key Management Challenge**:

With traditional public key cryptography, the generation of the keys,
the publication of the associations between parties and their public keys and
the management of all this require a dedicated secure infrastructure.
Such an infrastructure is expensive, complex, does not scale well to large sizes,
and does not easily extend to manage parties’ attributes, e.g., their roles and rights.
Such issues have not been solved, despite years of attempts – this has
limited the take-up of public key cryptography.

**Motivation**:

IBE offers a much simpler solution for many applications, solving the above challenge.
And two reasons are elaborated as follows.

**First Resaon**:

Because the encryption key can be any bit string, it can be chosen by
the encrypting party. The encrypting party can base its choice of bit
string on the needs of the application. First choice is something simple, e.g,
the email address of the receiving party, a digital photograph of the receiving party, a URL.
Second choice is something more complex, e.g,
the role of the receiving party, expressed by a list
of attributes he must have, a set of conditions the receiving party must meet,
a policy that the receiving party must conform to, executable program code.

Expressing these requirements in the encryption key relieves the
supporting infrastructure from managing them, thus enabling the
infrastructure to be simpler

**Second Reason**:

Because the decryption key does not need to be generated at
the same time, or by the same entity, as the encryption key, the
trusted third party can delay generating it until the receiving
party has demonstrated its right to have it.

So, there is no need for any party to store keys, thus, easing the management problem considerably, reducing the risk of inadvertently exposed keys
compromising the secrecy of the protected content.

A different key can be used, if desired, for every interaction
between the sending and receiving parties.

**Application**:

First is obscuring content by reversibly scrambling it, thus securing it against viewing by unauthorised parties. Second is signing content, thus making unrepudiable the link between the content and the signing party. Third is requiring the consent of multiple third parties (this consent being given, for example, only if the receiving party meets
multiple sets of conditions, at least one per third party) before decryption is possible.
