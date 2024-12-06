# repetitions

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Can you make sense of this file? <br>
Download the file [here](https://artifacts.picoctf.net/c/473/enc_flag).

## Approach

Upon reading the text in `enc_flag`, it seems to be base-64 encoded, so I used [Cyberchef](https://cyberchef.net/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=Vm1wR1UxRXlSWGxVV0d4VFlteEtWVll3WkZOV2JHeHlWMjFHVjFKdGVEQlViRnBQWVd4S2RGVnNhRnBXVmxVeFdWWmFTMVpXV25WaA0KUm1SWFpXdGFiMWRXV210U01rNXlUbFpXV0FwaVZWcFVWbTEwZDFWV1pGZFZhMlJwWWxaYVdGWnROVmRWWjNCcFUwVktlbGRXVWtOaw0KTWxaWFZsaG9XR0pZUWs5VmJGSlhVMFprY1ZSdVRsZGFNMEpaVldwR1MyVldXa2RhU0dSWENrMXNXbnBXVjNoaFZtMUtSazVYT1ZWVw0KVmtwRVZHeGFZVmRGTVZoU2JIQldWMFZLVlZaR1dtOVJNbFp6VjJ0V1VtSkZOVk5EYlVwWFYyNXdXbUV4U21oV01HUkhaRWRXUmxacw0KYUdrS1lsUnJlbFpFUmxkVU1rcHpVV3hXVGxKWVRreERaejA5Q2c9PQ&ieol=CRLF) to decode it.

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2023/General-Skills/repetitions/img/first.png" />
</p>

However, the output seems like another base-64 encoded text, so I repeatedly base-64 decoded it and obtained the flag after base-64 decoding it 6 times.

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2023/General-Skills/repetitions/img/flag.png" />
</p>

## Flag

`picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_dfe803c6}`