



with open("./print_lin.o", mode='rb') as file:
    magic_number = file.read(4)

    if magic_number != b'\x7fELF':
        print("incorrect file format!")
        exit(-1)

    print(magic_number)

    EI_CLASS = file.read(1)

    if EI_CLASS == b'\x01':
        print("32-bit instruction set")
    elif EI_CLASS == b'\x02':
        print("64 bit instruction set")
    else:
        print("not supported instruction set:", EI_CLASS)
        exit(-1)

    EI_DATA = file.read(1)

    if EI_DATA == b'\x01':
        print("little endianness")
    elif EI_DATA == b'\x02':
        print("big endianness")
    else:
        print("not supported:", EI_DATA)
        exit(-1)

    EI_VERSION = file.read(1)
    print("Elf version:", EI_VERSION)

    # ===============================================================+
    # Target operating system                                        |
    # 0x00	System V                                             |
    # 0x01	HP-UX
    # 0x02	NetBSD
    # 0x03	Linux
    # 0x04	GNU Hurd
    # 0x06	Solaris
    # 0x07	AIX
    # 0x08	IRIX
    # 0x09	FreeBSD
    # 0x0A	Tru64
    # 0x0B	Novell Modesto
    # 0x0C	OpenBSD
    # 0x0D	OpenVMS
    # 0x0E	NonStop Kernel
    # 0x0F	AROS
    # 0x10	Fenix OS
    # 0x11	CloudABI
    # 0x12	Stratus Technologies OpenVOS

    EI_OSABI = file.read(1)    
    if not (EI_OSABI == b'\x03' or EI_OSABI == b'\x00'):
        print("Only Linux is supported")
        exit(-1)
    # ==============================================================
    
    EI_ABIVERSION = file.read(1)
    print("EI_ABIVERSION:", EI_ABIVERSION)
    
    # it is not userd should be 0
    EI_PAD = file.read(7)

    # ===============================================================
    # Object type file 
    # 0x00	ET_NONE
    # 0x01	ET_REL
    # 0x02	ET_EXEC
    # 0x03	ET_DYN
    # 0x04	ET_CORE
    # 0xFE00	ET_LOOS
    # 0xFEFF	ET_HIOS
    # 0xFF00	ET_LOPROC
    # 0xFFFF	ET_HIPROC

    e_type = file.read(2)
    print("e_type:", e_type)
    #==================================================================
    # Instruction set architecture
    # 0x00	No specific instruction set
    # 0x01	AT&T WE 32100
    # 0x02	SPARC
    # 0x03	x86
    # 0x04	Motorola 68000 (M68k)
    # 0x05	Motorola 88000 (M88k)
    # 0x06	Intel MCU
    # 0x07	Intel 80860
    # 0x08	MIPS
    # 0x09	IBM System/370
    # 0x0A	MIPS RS3000 Little-endian
    # 0x0B - 0x0D	Reserved for future use
    # 0x0E	Hewlett-Packard PA-RISC
    # 0x0F	Reserved for future use
    # 0x13	Intel 80960
    # 0x14	PowerPC
    # 0x15	PowerPC (64-bit)
    # 0x16	S390, including S390x
    # 0x17	IBM SPU/SPC
    # 0x18 - 0x23	Reserved for future use
    # 0x24	NEC V800
    # 0x25	Fujitsu FR20
    # 0x26	TRW RH-32
    # 0x27	Motorola RCE
    # 0x28	ARM (up to ARMv7/Aarch32)
    # 0x29	Digital Alpha
    # 0x2A	SuperH
    # 0x2B	SPARC Version 9
    # 0x2C	Siemens TriCore embedded processor
    # 0x2D	Argonaut RISC Core
    # 0x2E	Hitachi H8/300
    # 0x2F	Hitachi H8/300H
    # 0x30	Hitachi H8S
    # 0x31	Hitachi H8/500
    # 0x32	IA-64
    # 0x33	Stanford MIPS-X
    # 0x34	Motorola ColdFire
    # 0x35	Motorola M68HC12
    # 0x36	Fujitsu MMA Multimedia Accelerator
    # 0x37	Siemens PCP
    # 0x38	Sony nCPU embedded RISC processor
    # 0x39	Denso NDR1 microprocessor
    # 0x3A	Motorola Star*Core processor
    # 0x3B	Toyota ME16 processor
    # 0x3C	STMicroelectronics ST100 processor
    # 0x3D	Advanced Logic Corp. TinyJ embedded processor family
    # 0x3E	AMD x86-64
    # 0x8C	TMS320C6000 Family
    # 0xAF	MCST Elbrus e2k
    # 0xB7	ARM 64-bits (ARMv8/Aarch64)
    # 0xF3	RISC-V
    # 0xF7	Berkeley Packet Filter
    #0x101	WDC 65C816

    e_machine = file.read(2)
    print("e_machine", e_machine)
    #===========================================================
    e_version =  file.read(4)
    print("e_version", e_version)
    
    # starts parsing for 64 bit
    e_entry = file.read(8)
    print("e_entry", e_entry)

    e_phoff = file.read(8)
    print("e_phoff", e_phoff)

    e_shoff = file.read(8)
    print("e_shoff", e_shoff) 
