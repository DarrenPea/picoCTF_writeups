# Mr-Worldwide

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

A musician left us a [message](https://jupiter.challenges.picoctf.org/static/d5570d48262dbba2a31f2a940409ad9d/message.txt). What's it mean?

## Approach

Looking at the `message.txt`, it appears that the flag is being written in terms of longitude and latitude. Upon searching the locations based on longitude and latitude, I took the first letter of each city and obtained the flag.

```
(K)yoto, Japan 							// (35.028309, 135.753082)
(O)desa, Ukraine 						// (46.469391, 30.740883)
(D)ayton OH, United States 				// (39.758949, -84.191605)
(I)stanbul, Türkiye 					// (41.015137, 28.979530)
(A)bu Dhabi, United Arab Emirates		// (24.466667, 54.366669)
(K)uala Lumpur, Malaysia 				// (3.140853, 101.693207)
_
(A)ddis Ababa, Ethiopia 				// (9.005401, 38.763611)
(L)oja, Ecuador 						// (-3.989038, -79.203560)
(A)msterdam, Netherlands 				// (52.377956, 4.897070)
(S)leepy Hollow, United States 			// (41.085651, -73.858467)
(K)odiak, United States 				// (57.790001, -152.407227)
(A)lexandria, Egypt 					// (31.205753, 29.924526)
```


## Flag

`picoCTF{KODIAK_ALASKA}`