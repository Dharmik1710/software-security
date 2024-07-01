Some labs and topics covered


Setuid and effective user ID
File access attacks - Path Traversals, TOCTOU, file handler reuse
Memory corruption attacks - Stack corruption, heap corruption, format string exploitation, JIT compilation corruptions
	Non-terminal String overflow
	Index overflow
ASLR Exploitation
Bypassing stack canaries - using forking server
Overwriting Global Offset Tables(GOT) and mitigation
NOP sleds
Memory leaks - printf
Return oriented programming(ROP chain attacks)
Buffer overflows
Heap exploitation
Use after free attacks
SECCOMP
Address sanitizer(ASAN) - prevent use after free attacks
Automated analysis - 
	Dynamic analysis - fuzzing, 
	Static analysis - control-flow graph, Data-flow analysis, value-set analysis
	Symbolic execution - Forward SE, Under-constrained SE
American Fuzzy Lop(AFL and AFL++) - Random fuzzing, Grammar based fuzzing, graybox fuzzing
Angr - symbollic execution
Rust 
	Ownership and functions
	Mutable and immutable references
	Rust Security
Android
	Compilation
	App reverse engineering
	App dynamic analysis - Frida Framework
	App execution
	Permission groups and Permission enforcement
	Binder
	App/System interaction
	Security principle - google rule of 2
		code with untrustworthy input
		code which runs with no sandbox
		code written in unsafe language
	Execution environments - contexts
		Isolated Processes
		Normal Apps
		System Apps
		System Services
		Linux kernel
		Bootloader
		TrustZone(TEE)
		Secure Element(SE)

Credits - Antonio Bianchi, Software Security(CS527) (Depart of Computer Science, Purdue University)
