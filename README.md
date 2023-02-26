# VulnServer Buffer-Overflows Attack



> cat trun.spk
<img src="https://github.com/thund3rb0lt0x1/Buffer-Overflows/blob/main/Assets/trun.png" alt="Spiking" width="320">


It sends bunch of AAA's same as fuzzing, till the vulnserver crashes.
<img src="https://github.com/thund3rb0lt0x1/Buffer-Overflows/blob/main/Assets/generic_send_tcp.png" alt="Generic_send_tcp" width="580">

We are sending bunch of AAA's till the vulnserver crashes.
<img src="https://github.com/thund3rb0lt0x1/Buffer-Overflows/blob/main/Assets/Fuzzing.png" alt="Fuzzing" width="780">

Now we don't know that where exactly EIP is at, But note down on how many bytes the server was crashed.

Now create random code using pattern_create.
> msf-pattern_create -l 2200
<img src="https://github.com/thund3rb0lt0x1/Buffer-Overflows/blob/main/Assets/Offset_2.png" alt="Offset" width="780">

Lets run the script to get the EIP address.

<img src="https://github.com/thund3rb0lt0x1/Buffer-Overflows/blob/main/Assets/EIP_immunity.png" alt="EIP_Addr" width="780">

It will show where the server is crashed exactly.

<img src="https://github.com/thund3rb0lt0x1/Buffer-Overflows/blob/main/Assets/pattern_offset.png" alt="Pattern_offset" width="480">

It should break the program, As you can see the EIP is overwritten with 42424242 that is 4 B's.<br>
So now we can control EIP now.
<img src="https://github.com/thund3rb0lt0x1/Buffer-Overflows/blob/main/Assets/Controlling_EIP.png" alt="Controlling_EIP" width="780">

First go to 'C:\' drive and create a folder called 'mona'
Now in Immunity debugger type
> !mona config -set workingfolder C:\mona

Now, once we have our workingfolder set, now going to generate a Bad characters list.
> !mona bytearray -cpb '\x00'

Now go to the folder 'C:\mona' you will see there will be 2 files one is 'bytearray.bin' and 'bytearray.txt' files.
If you open bytearray.txt file you will see the bytearray is generated, we can copy the badcharacters and past in python script.

<img src="https://github.com/thund3rb0lt0x1/Buffer-Overflows/blob/main/Assets/Finding_badchars.png" alt="Finding_Badchars" width="780">

Now hope fully we should crash the software.<br>
Note down the <b>ESP address<b>

<img src="https://github.com/thund3rb0lt0x1/Buffer-Overflows/blob/main/Assets/badchars_ESP.png" alt="ESP_Badchars" width="780">

Type in Immunity
> !mona compare -f C:\mona\bytearray.bin -a <ESP_address>

Now it will look for any badcharacters and display in 'BadChars' column.
<img src="https://github.com/thund3rb0lt0x1/Buffer-Overflows/blob/main/Assets/immunity_badchars.png" alt="Immunity_Badchars" width="780">

Now we have to find our jump addr / return addr
> !mona modules
<img src="https://github.com/thund3rb0lt0x1/Buffer-Overflows/blob/main/Assets/mona_modules.png" alt="Mona_Modules" width="780">

> !mona jmp -r ESP -m "essfunc.dll"

Now lets see the return address after minimizing the 'CPU threads' in 'Log data' tab.
In see in <b>'Results:' Address is '0x625011af'<b>
<img src="https://github.com/thund3rb0lt0x1/Buffer-Overflows/blob/main/Assets/return_addr.png" alt="Return_Addr" width="780">

In the script we have entered the return addr in reverse order (i.e Little endian format) : <b>'\xaf\x11\x50\x62'<b>
<img src="https://github.com/thund3rb0lt0x1/Buffer-Overflows/blob/main/Assets/getting_shell.png" alt="Getting_Shell" width="780">

Getting reverse shell!!
<img src="https://github.com/thund3rb0lt0x1/Buffer-Overflows/blob/main/Assets/netcat.png" alt="NetCat" width="780">
