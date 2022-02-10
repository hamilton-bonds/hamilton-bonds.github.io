---
title: "[250] We're Related (Cryptography)"
layout: template
filename: wererelated.md
---

## [250] We're Related (Cryptography)

### Prompt:
Recently, the Beacon Messenger App added support for one-time-read, 'disappearing' messages. We need you to find a flaw in their implementation, then decrypt an intercepted message provided to you upon connection. challenge.acictf.com:46218 messenger.py (NOTE: Your port may be different)

### Initial Analysis:
(Solved during training)

Looking at each of the functions in messenger.py, we can see from a cursory analysis that the server encodes messages sent between Alice and Bob with a large-number RSA encryption.  When we query the server for the key (input: "KEY:"), we get

```
N=27607181346013830729177284887939356716222828873207125661601723895320362970647047547219526423409390082642386604683385000602817163383821976918928284014105987401614862431837215798914594399761070594339941056964035988333614149177576256407639955414210046388281622359875360181382847153865439484081184012046769264419216122103860197910941752961915383598012613257787952538710995791614723882907931290465484850197183654625460255077707494174998315828857018481731061240797541378157880606978824480150401199153996445207228487684415653273726315905420295655900863579952611810813862184604558680084775761797027831631147651130620872798651
e=65537
```

Large numbers are not fun to work with in RSA, so let's look at messenger.py again to see what else we notice.



### Solution:



END
