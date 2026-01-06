; ------------- ____syscall_malloc --------------

   0x0000000000001300 <+0>:	push   rbp
   0x0000000000001301 <+1>:	mov    rbp,rsp
   0x0000000000001304 <+4>:	lea    rdi,[rip+0xd2e]        # 0x2039
   0x000000000000130b <+11>:	call   0x1030 <puts@plt>      # print "Good job."
   0x0000000000001310 <+16>:	pop    rbp
   0x0000000000001311 <+17>:	ret                           # return

; ------------- ___syscall_malloc --------------

   0x00000000000012e0 <+0>:	push   rbp
   0x00000000000012e1 <+1>:	mov    rbp,rsp
   0x00000000000012e4 <+4>:	lea    rdi,[rip+0xd48]        # 0x2033
   0x00000000000012eb <+11>:	call   0x1030 <puts@plt>      # print "Nope."
   0x00000000000012f0 <+16>:	mov    edi,0x1
   0x00000000000012f5 <+21>:	call   0x10b0 <exit@plt>      # return


; ------------- main --------------

   0x0000555555555320 <+0>:	push   rbp
   0x0000555555555321 <+1>:	mov    rbp,rsp
   0x0000555555555324 <+4>:	sub    rsp,0x60
   0x0000555555555328 <+8>:	mov    DWORD PTR [rbp-0x4],0x0				# set input buffer
   0x000055555555532f <+15>:	lea    rdi,[rip+0xd0d]        
   0x0000555555555336 <+22>:	mov    al,0x0
   0x0000555555555338 <+24>:	call   0x555555555050 <printf@plt>   		# Print "Please enter key: "
   0x000055555555533d <+29>:	lea    rsi,[rbp-0x40]
   0x0000555555555341 <+33>:	lea    rdi,[rip+0xd0e]        
   0x0000555555555348 <+40>:	mov    al,0x0
   0x000055555555534a <+42>:	call   0x5555555550a0 <__isoc99_scanf@plt> 	# Scan for input scanf("%23s"), store in 0x40
   0x000055555555534f <+47>:	mov    DWORD PTR [rbp-0x8],eax				# rbp-0x8 = last 2 bytes of scanf returns
   0x0000555555555352 <+50>:	mov    eax,0x1							        	# eax = 1
   0x0000555555555357 <+55>:	cmp    eax,DWORD PTR [rbp-0x8]				# compare scanf return value with 1
   0x000055555555535a <+58>:	je     0x555555555365 <main+69>				# if scanf = 1 jump 🟥
   0x0000555555555360 <+64>:	call   0x5555555552e0 <___syscall_malloc> # 🚫 Fail function
   0x0000555555555365 <+69>:	movsx  ecx,BYTE PTR [rbp-0x3f]				# 🟥 ecx = buffer[1] (0x40 + 1)
   0x0000555555555369 <+73>:	mov    eax,0x32							   	# eax = 50 = "2"
   0x000055555555536e <+78>:	cmp    eax,ecx								      # compare input[1] with "2"
   0x0000555555555370 <+80>:	je     0x55555555537b <main+91>				# if input[1] == "2" jump 🟦
   0x0000555555555376 <+86>:	call   0x5555555552e0 <___syscall_malloc> # 🚫 Fail function
   0x000055555555537b <+91>:	movsx  ecx,BYTE PTR [rbp-0x40]				# 🟦 ecx = 0x40 = input[0]
   0x000055555555537f <+95>:	mov    eax,0x34                           # eax = 52 = "4"
   0x0000555555555384 <+100>:	cmp    eax,ecx                            # compare 
   0x0000555555555386 <+102>:	je     0x555555555391 <main+113>          # 🟧 if (input[0] == "4")
   0x000055555555538c <+108>:	call   0x5555555552e0 <___syscall_malloc> # 🚫 Fail function
   0x0000555555555391 <+113>:	mov    rax,QWORD PTR [rip+0x2c48]        #  🟧 
   0x0000555555555398 <+120>:	mov    rdi,QWORD PTR [rax]
   0x000055555555539b <+123>:	call   0x555555555080 <fflush@plt>
   0x00005555555553a0 <+128>:	lea    rdi,[rbp-0x21]                     # init buffer at 0x21
   0x00005555555553a4 <+132>:	xor    esi,esi                            # esi = 0
   0x00005555555553a6 <+134>:	mov    edx,0x9                            # edx = 9
   0x00005555555553ab <+139>:	call   0x555555555060 <memset@plt>        # memset(buffer, 0, 9)
   0x00005555555553b0 <+144>:	mov    BYTE PTR [rbp-0x21],0x2a           # buffer[0] = 42 = "*"
   0x00005555555553b4 <+148>:	mov    BYTE PTR [rbp-0x41],0x0            # 0x41 = 0 => buffer[9]
   0x00005555555553b8 <+152>:	mov    QWORD PTR [rbp-0x18],0x2           # 0x18 = 2 (counter i)
   0x00005555555553c0 <+160>:	mov    DWORD PTR [rbp-0xc],0x1            # 0xc = 1  (counter j)
   0x00005555555553c7 <+167>:	lea    rdi,[rbp-0x21]                     # rdi = &buffer[0] | loop start ⚪ 
   0x00005555555553cb <+171>:	call   0x555555555040 <strlen@plt>        # strlen(buffer)
   0x00005555555553d0 <+176>:	mov    rcx,rax                             
   0x00005555555553d3 <+179>:	xor    eax,eax
   0x00005555555553d5 <+181>:	cmp    rcx,0x8                            # compare strlen(buffer) with 8
   0x00005555555553d9 <+185>:	mov    BYTE PTR [rbp-0x45],al             #  
   0x00005555555553dc <+188>:	jae    0x555555555403 <main+227>          # if (strlen(buffer) >= 8) jump 🟩
   0x00005555555553e2 <+194>:	mov    rax,QWORD PTR [rbp-0x18]           # rax = i
   0x00005555555553e6 <+198>:	mov    QWORD PTR [rbp-0x50],rax
   0x00005555555553ea <+202>:	lea    rdi,[rbp-0x40]                     # load input
   0x00005555555553ee <+206>:	call   0x555555555040 <strlen@plt>        # strlen(input)
   0x00005555555553f3 <+211>:	mov    rcx,rax                            
   0x00005555555553f6 <+214>:	mov    rax,QWORD PTR [rbp-0x50]           
   0x00005555555553fa <+218>:	cmp    rax,rcx                            # compare i and strlen(input)
   0x00005555555553fd <+221>:	setb   al                                 # set al = 1 if below => i < strlen(input) ? al = 1 : al = 0 
   0x0000555555555400 <+224>:	mov    BYTE PTR [rbp-0x45],al
   0x0000555555555403 <+227>:	mov    al,BYTE PTR [rbp-0x45]             # 🟩
   0x0000555555555406 <+230>:	test   al,0x1                             # test al => al & 1
   0x0000555555555408 <+232>:	jne    0x555555555413 <main+243>          # if not zero flag jump 🟪 
   0x000055555555540e <+238>:	jmp    0x555555555461 <main+321>          # else jump 🟫
   0x0000555555555413 <+243>:	mov    rax,QWORD PTR [rbp-0x18]           # 🟪 rax = i counter
   0x0000555555555417 <+247>:	mov    al,BYTE PTR [rbp+rax*1-0x40]       # load input + i in al
   0x000055555555541b <+251>:	mov    BYTE PTR [rbp-0x44],al             # load in new buffer => temp[0] = input[0]
   0x000055555555541e <+254>:	mov    rax,QWORD PTR [rbp-0x18]
   0x0000555555555422 <+258>:	mov    al,BYTE PTR [rbp+rax*1-0x3f]       # temp[1] = input[i + 1]
   0x0000555555555426 <+262>:	mov    BYTE PTR [rbp-0x43],al
   0x0000555555555429 <+265>:	mov    rax,QWORD PTR [rbp-0x18]
   0x000055555555542d <+269>:	mov    al,BYTE PTR [rbp+rax*1-0x3e]       # temp[1] = input[i + 2]
   0x0000555555555431 <+273>:	mov    BYTE PTR [rbp-0x42],al
   0x0000555555555434 <+276>:	lea    rdi,[rbp-0x44]                     # load temp
   0x0000555555555438 <+280>:	call   0x555555555090 <atoi@plt>          # atoi(temp)
   0x000055555555543d <+285>:	mov    cl,al                              # takes 8 last bits of atoi result
   0x000055555555543f <+287>:	movsxd rax,DWORD PTR [rbp-0xc]            
   0x0000555555555443 <+291>:	mov    BYTE PTR [rbp+rax*1-0x21],cl       # buf[j] = 8 last bit of atoi (char)
   0x0000555555555447 <+295>:	mov    rax,QWORD PTR [rbp-0x18]           # rax = i
   0x000055555555544b <+299>:	add    rax,0x3                            # i += 3
   0x000055555555544f <+303>:	mov    QWORD PTR [rbp-0x18],rax
   0x0000555555555453 <+307>:	mov    eax,DWORD PTR [rbp-0xc]            # load j in eax
   0x0000555555555456 <+310>:	add    eax,0x1                            # j += 1
   0x0000555555555459 <+313>:	mov    DWORD PTR [rbp-0xc],eax
   0x000055555555545c <+316>:	jmp    0x5555555553c7 <main+167>          # Loop ⚪
   0x0000555555555461 <+321>:	movsxd rax,DWORD PTR [rbp-0xc]            # 🟫
   0x0000555555555465 <+325>:	mov    BYTE PTR [rbp+rax*1-0x21],0x0
   0x000055555555546a <+330>:	lea    rsi,[rip+0xb93]        
   0x0000555555555471 <+337>:	lea    rdi,[rbp-0x21]                    # load buffer
   0x0000555555555475 <+341>:	call   0x555555555070 <strcmp@plt>       # strcmp("********", &buffer[0])
   0x000055555555547a <+346>:	mov    DWORD PTR [rbp-0x10],eax          # 0x10 = strcmp 
   0x000055555555547d <+349>:	mov    eax,DWORD PTR [rbp-0x10]           
   0x0000555555555480 <+352>:	mov    DWORD PTR [rbp-0x54],eax          # 0x54 = strcmp (new variable *comp)
   0x0000555555555483 <+355>:	sub    eax,0xfffffffe                    # 0xfffffffe = -2 (32-bit value) comp -= -2
   # sub set ZF if result = 0, SF for sign result, OF sign overflow and CF if unsign overflow
   0x0000555555555486 <+358>:	je     0x555555555536 <main+534>         # jump if ZF = 1 so if 0x54 = -2 jump fail 🚫
   0x000055555555548c <+364>:	jmp    0x555555555491 <main+369>         # else 
   0x0000555555555491 <+369>:	mov    eax,DWORD PTR [rbp-0x54]          
   0x0000555555555494 <+372>:	sub    eax,0xffffffff                    # result = comp - -1
   0x0000555555555497 <+375>:	je     0x55555555552c <main+524>         # if result == 0 jump fail 🚫
   0x000055555555549d <+381>:	jmp    0x5555555554a2 <main+386>
   0x00005555555554a2 <+386>:	mov    eax,DWORD PTR [rbp-0x54]
   0x00005555555554a5 <+389>:	test   eax,eax                           # result = comp 
   0x00005555555554a7 <+391>:	je     0x55555555555e <main+574>         # jump if ZF (eax & eax == 0) Good job function ✅ 
   0x00005555555554ad <+397>:	jmp    0x5555555554b2 <main+402>         # else
   0x00005555555554b2 <+402>:	mov    eax,DWORD PTR [rbp-0x54]
   0x00005555555554b5 <+405>:	sub    eax,0x1                            # result = comp - 1
   0x00005555555554b8 <+408>:	je     0x555555555518 <main+504>          # jump if resuilt == 0 to fail 🚫
   0x00005555555554be <+414>:	jmp    0x5555555554c3 <main+419>          # else
   0x00005555555554c3 <+419>:	mov    eax,DWORD PTR [rbp-0x54]           
   0x00005555555554c6 <+422>:	sub    eax,0x2                            # result = comp - 2
   0x00005555555554c9 <+425>:	je     0x555555555522 <main+514>          # if result == 0 jump to fail 🚫
   0x00005555555554cf <+431>:	jmp    0x5555555554d4 <main+436>          # else
   0x00005555555554d4 <+436>:	mov    eax,DWORD PTR [rbp-0x54]
   0x00005555555554d7 <+439>:	sub    eax,0x3                            # result = comp - 3
   0x00005555555554da <+442>:	je     0x555555555540 <main+544>          # if result == 0 jump to fail 🚫
   0x00005555555554e0 <+448>:	jmp    0x5555555554e5 <main+453>          # else
   0x00005555555554e5 <+453>:	mov    eax,DWORD PTR [rbp-0x54]
   0x00005555555554e8 <+456>:	sub    eax,0x4                            # result = comp - 4
   0x00005555555554eb <+459>:	je     0x55555555554a <main+554>          # if result == 0 jump to fail 🚫
   0x00005555555554f1 <+465>:	jmp    0x5555555554f6 <main+470>          # else
   0x00005555555554f6 <+470>:	mov    eax,DWORD PTR [rbp-0x54]
   0x00005555555554f9 <+473>:	sub    eax,0x5                            # result = comp - 5
   0x00005555555554fc <+476>:	je     0x555555555554 <main+564>          # if result == 0 jump to fail 🚫
   0x0000555555555502 <+482>:	jmp    0x555555555507 <main+487>          # else
   0x0000555555555507 <+487>:	mov    eax,DWORD PTR [rbp-0x54]
   0x000055555555550a <+490>:	sub    eax,0x73                           # result = comp - 73
   0x000055555555550d <+493>:	je     0x555555555568 <main+584>          # if result == 0 jump to fail 🚫
   0x0000555555555513 <+499>:	jmp    0x555555555572 <main+594>          # jump to fail 🚫
   0x0000555555555518 <+504>:	call   0x5555555552e0 <___syscall_malloc>    # 🚫 Fail function
   0x000055555555551d <+509>:	jmp    0x555555555577 <main+599>
   0x0000555555555522 <+514>:	call   0x5555555552e0 <___syscall_malloc>    # 🚫 Fail function
   0x0000555555555527 <+519>:	jmp    0x555555555577 <main+599>
   0x000055555555552c <+524>:	call   0x5555555552e0 <___syscall_malloc>    # 🚫 Fail function
   0x0000555555555531 <+529>:	jmp    0x555555555577 <main+599>
   0x0000555555555536 <+534>:	call   0x5555555552e0 <___syscall_malloc>    # 🚫 Fail function
   0x000055555555553b <+539>:	jmp    0x555555555577 <main+599>
   0x0000555555555540 <+544>:	call   0x5555555552e0 <___syscall_malloc>    # 🚫 Fail function
   0x0000555555555545 <+549>:	jmp    0x555555555577 <main+599>
   0x000055555555554a <+554>:	call   0x5555555552e0 <___syscall_malloc>    # 🚫 Fail function
   0x000055555555554f <+559>:	jmp    0x555555555577 <main+599>
   0x0000555555555554 <+564>:	call   0x5555555552e0 <___syscall_malloc>    # 🚫 Fail function
   0x0000555555555559 <+569>:	jmp    0x555555555577 <main+599>
   0x000055555555555e <+574>:	call   0x555555555300 <____syscall_malloc>   # ✅ Good job function (different address)
   0x0000555555555563 <+579>:	jmp    0x555555555577 <main+599>
   0x0000555555555568 <+584>:	call   0x5555555552e0 <___syscall_malloc>    # 🚫 Fail function
   0x000055555555556d <+589>:	jmp    0x555555555577 <main+599>
   0x0000555555555572 <+594>:	call   0x5555555552e0 <___syscall_malloc>    # 🚫 Fail function
   0x0000555555555577 <+599>:	xor    eax,eax                               # Set eax to 0
   0x0000555555555579 <+601>:	add    rsp,0x60   
   0x000055555555557d <+605>:	pop    rbp                                   # return(0)
   0x000055555555557e <+606>:	ret


; # ---------------- PATCH -------------------
; Change fail function (___syscall_malloc)
; to "Good job." and exit(0)