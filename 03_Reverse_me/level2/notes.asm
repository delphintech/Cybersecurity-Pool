0x000012d0 <+0>:	push   ebp
   0x000012d1 <+1>:	mov    ebp,esp
   0x000012d3 <+3>:	push   ebx'
   0x000012d4 <+4>:	sub    esp,0x54
   0x000012d7 <+7>:	call   0x12dc <main+12>
   0x000012dc <+12>:	pop    ebx
   0x000012dd <+13>:	add    ebx,0x5d24
   0x000012e3 <+19>:	mov    DWORD PTR [ebp-0x40],ebx           # 0x40 = 0x5d24
   0x000012e6 <+22>:	mov    DWORD PTR [ebp-0x8],0x0
   0x000012ed <+29>:	lea    eax,[ebx-0x42e5]
   0x000012f3 <+35>:	mov    DWORD PTR [esp],eax
   0x000012f6 <+38>:	call   0x1060 <printf@plt>                # "Enter Key: "
   0x000012fb <+43>:	mov    ebx,DWORD PTR [ebp-0x40]
   0x000012fe <+46>:	lea    eax,[ebp-0x35]
   0x00001301 <+49>:	lea    ecx,[ebx-0x42d2]
   0x00001307 <+55>:	mov    DWORD PTR [esp],ecx
   0x0000130a <+58>:	mov    DWORD PTR [esp+0x4],eax
   0x0000130e <+62>:	call   0x10c0 <__isoc99_scanf@plt>        # Scan for input
   0x00001313 <+67>:	mov    DWORD PTR [ebp-0xc],eax
   0x00001316 <+70>:	mov    eax,0x1
   0x0000131b <+75>:	cmp    eax,DWORD PTR [ebp-0xc]            # Compare le retour de Scanf avec 1
   0x0000131e <+78>:	je     0x132c <main+92>                   # IF scanf == 1 Jump to 92 🟥
   0x00001324 <+84>:	mov    ebx,DWORD PTR [ebp-0x40]
   0x00001327 <+87>:	call   0x1220 <no>                        # Else scanf != 1 => No() 🚫
   0x0000132c <+92>:	movsx  ecx,BYTE PTR [ebp-0x34]            # 🟥 take input[1]
   0x00001330 <+96>:	mov    eax,0x30                           
   0x00001335 <+101>:	cmp    eax,ecx                         # Compare input[1] with "0" (ascii 30)
   0x00001337 <+103>:	je     0x1345 <main+117>               # If equal (input[1] == "0") jump 🟦
   0x0000133d <+109>:	mov    ebx,DWORD PTR [ebp-0x40]        
   0x00001340 <+112>:	call   0x1220 <no>                     # Else no() 🚫
   0x00001345 <+117>:	movsx  ecx,BYTE PTR [ebp-0x35]         # 🟦 take input[0]
   0x00001349 <+121>:	mov    eax,0x30
   0x0000134e <+126>:	cmp    eax,ecx                         # Compare input[1] with "0" (ascii 30)
   0x00001350 <+128>:	je     0x135e <main+142>               # If equal (input[1] == "0") jump ◻️
   0x00001356 <+134>:	mov    ebx,DWORD PTR [ebp-0x40]
   0x00001359 <+137>:	call   0x1220 <no>                     # Else no() 🚫
   0x0000135e <+142>:	mov    ebx,DWORD PTR [ebp-0x40]        # ⬜
   0x00001361 <+145>:	mov    eax,DWORD PTR [ebx-0xc]
   0x00001367 <+151>:	mov    eax,DWORD PTR [eax]
   0x00001369 <+153>:	mov    ecx,DWORD PTR [ebx-0xc]
   0x0000136f <+159>:	mov    DWORD PTR [esp],eax
   0x00001372 <+162>:	call   0x1070 <fflush@plt>
   0x00001377 <+167>:	mov    ebx,DWORD PTR [ebp-0x40]
   0x0000137a <+170>:	lea    eax,[ebp-0x1d]
   0x0000137d <+173>:	xor    ecx,ecx
   0x0000137f <+175>:	mov    DWORD PTR [esp],eax
   0x00001382 <+178>:	mov    DWORD PTR [esp+0x4],0x0
   0x0000138a <+186>:	mov    DWORD PTR [esp+0x8],0x9
   0x00001392 <+194>:	call   0x10b0 <memset@plt>
   0x00001397 <+199>:	mov    BYTE PTR [ebp-0x1d],0x64        # 0x1d = "d"
   0x0000139b <+203>:	mov    BYTE PTR [ebp-0x36],0x0         # 0x36 = 0
   0x0000139f <+207>:	mov    DWORD PTR [ebp-0x14],0x2        # 0x14 = 2
   0x000013a6 <+214>:	mov    DWORD PTR [ebp-0x10],0x1        # 0x10 = 1
   0x000013ad <+221>:	mov    ebx,DWORD PTR [ebp-0x40]
   0x000013b0 <+224>:	lea    ecx,[ebp-0x1d]                  # set ecx = 0x1d = "d"
   0x000013b3 <+227>:	mov    eax,esp                        
   0x000013b5 <+229>:	mov    DWORD PTR [eax],ecx
   0x000013b7 <+231>:	call   0x10a0 <strlen@plt>             # strlen("d")
   0x000013bc <+236>:	mov    ecx,eax                   
   0x000013be <+238>:	xor    eax,eax
   0x000013c0 <+240>:	cmp    ecx,0x8                        # Compare strlen("d") avec 8
   0x000013c3 <+243>:	mov    BYTE PTR [ebp-0x41],al
   0x000013c6 <+246>:	jae    0x13ee <main+286>               # Si above ou equal jump 🟧 IMPOSSIBLE
   0x000013cc <+252>:	mov    ebx,DWORD PTR [ebp-0x40]        
   0x000013cf <+255>:	mov    eax,DWORD PTR [ebp-0x14]        
   0x000013d2 <+258>:	mov    DWORD PTR [ebp-0x48],eax        # 0x48 = eax = 0x14 = 2
   0x000013d5 <+261>:	lea    ecx,[ebp-0x35]                  # ecx = input[0]
   0x000013d8 <+264>:	mov    eax,esp
   0x000013da <+266>:	mov    DWORD PTR [eax],ecx
   0x000013dc <+268>:	call   0x10a0 <strlen@plt>             # strlen(input)
   0x000013e1 <+273>:	mov    ecx,eax                         
   0x000013e3 <+275>:	mov    eax,DWORD PTR [ebp-0x48]        # eax = 0x48 = 2
   0x000013e6 <+278>:	cmp    eax,ecx                         # compare strlen(input) with eax 
   0x000013e8 <+280>:	setb   al                              # set if below    al (low bit eax) => 0x48 < strlen(input) ? al = 1 : al = 0 
   0x000013eb <+283>:	mov    BYTE PTR [ebp-0x41],al
   0x000013ee <+286>:	mov    al,BYTE PTR [ebp-0x41]         # 🟧 
   0x000013f1 <+289>:	test   al,0x1                         # test (al & 1) == 1 so Zero flal = 0
   0x000013f3 <+291>:	jne    0x13fe <main+302>              #  jne => jump if Zero Flag = 0 🟩
   0x000013f9 <+297>:	jmp    0x144a <main+378>              # else (0x48 > strlen(input)  🟪
   0x000013fe <+302>:	mov    ebx,DWORD PTR [ebp-0x40]       # 🟩 
   0x00001401 <+305>:	mov    eax,DWORD PTR [ebp-0x14]
   0x00001404 <+308>:	mov    al,BYTE PTR [ebp+eax*1-0x35]
   0x00001408 <+312>:	mov    BYTE PTR [ebp-0x39],al         
   0x0000140b <+315>:	mov    eax,DWORD PTR [ebp-0x14]
   0x0000140e <+318>:	mov    al,BYTE PTR [ebp+eax*1-0x34]
   0x00001412 <+322>:	mov    BYTE PTR [ebp-0x38],al
   0x00001415 <+325>:	mov    eax,DWORD PTR [ebp-0x14]
   0x00001418 <+328>:	mov    al,BYTE PTR [ebp+eax*1-0x33]
   0x0000141c <+332>:	mov    BYTE PTR [ebp-0x37],al
   0x0000141f <+335>:	lea    eax,[ebp-0x39]
   0x00001422 <+338>:	mov    DWORD PTR [esp],eax
   0x00001425 <+341>:	call   0x10d0 <atoi@plt>
   0x0000142a <+346>:	mov    cl,al
   0x0000142c <+348>:	mov    eax,DWORD PTR [ebp-0x10]
   0x0000142f <+351>:	mov    BYTE PTR [ebp+eax*1-0x1d],cl
   0x00001433 <+355>:	mov    eax,DWORD PTR [ebp-0x14]
   0x00001436 <+358>:	add    eax,0x3
   0x00001439 <+361>:	mov    DWORD PTR [ebp-0x14],eax
   0x0000143c <+364>:	mov    eax,DWORD PTR [ebp-0x10]
   0x0000143f <+367>:	add    eax,0x1
   0x00001442 <+370>:	mov    DWORD PTR [ebp-0x10],eax
   0x00001445 <+373>:	jmp    0x13ad <main+221> 
   0x0000144a <+378>:	mov    ebx,DWORD PTR [ebp-0x40]        # 🟪
   0x0000144d <+381>:	mov    eax,DWORD PTR [ebp-0x10]
   0x00001450 <+384>:	mov    BYTE PTR [ebp+eax*1-0x1d],0x0
   0x00001455 <+389>:	lea    ecx,[ebp-0x1d]
   0x00001458 <+392>:	lea    edx,[ebx-0x42cd]
   0x0000145e <+398>:	mov    eax,esp
   0x00001460 <+400>:	mov    DWORD PTR [eax+0x4],edx
   0x00001463 <+403>:	mov    DWORD PTR [eax],ecx
   0x00001465 <+405>:	call   0x1040 <strcmp@plt>
   0x0000146a <+410>:	cmp    eax,0x0
   0x0000146d <+413>:	jne    0x1480 <main+432>
   0x00001473 <+419>:	mov    ebx,DWORD PTR [ebp-0x40]
   0x00001476 <+422>:	call   0x12a0 <ok>
   0x0000147b <+427>:	jmp    0x1488 <main+440>
   0x00001480 <+432>:	mov    ebx,DWORD PTR [ebp-0x40]
   0x00001483 <+435>:	call   0x1220 <no>
   0x00001488 <+440>:	xor    eax,eax
   0x0000148a <+442>:	add    esp,0x54
   0x0000148d <+445>:	pop    ebx
   0x0000148e <+446>:	pop    ebp
   0x0000148f <+447>:	ret    
