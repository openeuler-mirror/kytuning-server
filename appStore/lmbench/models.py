from django.db import models
import django.utils.timezone as timezone


# Create your models here.
class Lmbench(models.Model):
    """Lmbench表"""
    env_id = models.IntegerField(verbose_name='环境id')
    execute_cmd = models.CharField(null=True, blank=True, max_length=255, verbose_name='执行命令')
    modify_parameters = models.CharField(null=True, blank=True, max_length=255, verbose_name='修改参数')
    basic_Mhz = models.FloatField(verbose_name="Basic system parameters, Mhz")
    basic_tlb_pages = models.FloatField(verbose_name="Basic system parameters, tlb pages")
    basic_cache_line_bytes = models.FloatField(null=True, blank=True, verbose_name="Basic system parameters, cache line bytes")
    basic_mem_par = models.FloatField(null=True, blank=True, verbose_name="Basic system parameters, mem par")
    basic_scal_load = models.FloatField(verbose_name="Basic system parameters, scal load")
    processor_null_call = models.FloatField(verbose_name="Processor, null call")
    processor_null_I_O = models.FloatField(verbose_name="Processor, null I/O")
    processor_stat = models.FloatField(verbose_name="Processor, stat")
    processor_open_clo = models.FloatField(verbose_name="Processor, open clo")
    processor_slct_TCP = models.FloatField(verbose_name="Processor, slct TCP")
    processor_sig_inst = models.FloatField(verbose_name="Processor, sig inst")
    processor_sig_hndl = models.FloatField(verbose_name="Processor, sig hndl")
    processor_fork_proc = models.FloatField(verbose_name="Processor, fork proc")
    processor_exec_proc = models.FloatField(verbose_name="Processor, exec proc")
    processor_sh_proc = models.FloatField(verbose_name="Processor, sh proc")
    processor_Mhz = models.FloatField(verbose_name="Processor, Mhz")
    basic_intgr_bit = models.FloatField(verbose_name="Basic integer operations, intgr bit")
    basic_intgr_add = models.FloatField(verbose_name="Basic integer operations, intgr add")
    basic_intgr_mul = models.FloatField(verbose_name="Basic integer operations, intgr mul")
    basic_intgr_div = models.FloatField(verbose_name="Basic integer operations, intgr div")
    basic_intgr_mod = models.FloatField(verbose_name="Basic integer operations, intgr mod")
    basic_int64_bit = models.FloatField(verbose_name="Basic integer operations, int64 bit")
    basic_int64_add = models.FloatField(verbose_name="Basic integer operations, int64 add")
    basic_int64_mul = models.FloatField(verbose_name="Basic integer operations, int64 mul")
    basic_int64_div = models.FloatField(verbose_name="Basic integer operations, int64 div")
    basic_int64_mod = models.FloatField(verbose_name="Basic integer operations, int64 mod")
    basic_float_add = models.FloatField(verbose_name="Basic float operations, float add")
    basic_float_mul = models.FloatField(verbose_name="Basic float operations, float mul")
    basic_float_div = models.FloatField(verbose_name="Basic float operations, float div")
    basic_float_bogo = models.FloatField(verbose_name="Basic float operations, float bogo")
    basic_double_add = models.FloatField(verbose_name="Basic double operations, double add")
    basic_double_mul = models.FloatField(verbose_name="Basic double operations, double mul")
    basic_double_div = models.FloatField(verbose_name="Basic double operations, double div")
    basic_double_bogo = models.FloatField(verbose_name="Basic double operations, double bogo")
    context_2p_0K = models.FloatField(verbose_name="Context switching, 2p/0K")
    context_2p_16K = models.FloatField(verbose_name="Context switching, 2p/16K")
    context_2p_64K = models.FloatField(verbose_name="Context switching, 2p/64K")
    context_8p_16K = models.FloatField(verbose_name="Context switching, 8p/16K")
    context_8p_64K = models.FloatField(verbose_name="Context switching, 8p/64K")
    context_16p_16K = models.FloatField(verbose_name="Context switching, 16p/16K")
    context_16p_64K = models.FloatField(verbose_name="Context switching, 16p/64K")
    local_2p_0K = models.FloatField(verbose_name="*Local* Communication latencies, 2p/0K")
    local_Pipe = models.FloatField(verbose_name="*Local* Communication latencies, Pipe")
    local_AF_UNIX = models.FloatField(verbose_name="*Local* Communication latencies, AF UNIX")
    local_UDP = models.FloatField(verbose_name="*Local* Communication latencies, UDP")
    local_TCP = models.FloatField(verbose_name="*Local* Communication latencies, TCP")
    local_TCP_conn = models.FloatField(verbose_name="*Local* Communication latencies, TCP conn")
    local_RPC_TCP = models.FloatField(verbose_name="*Local* Communication latencies, RPC/TCP")
    local_RPC_UDP = models.FloatField(verbose_name="*Local* Communication latencies, RPC/UDP")
    local_bigger_Mmap_Latency = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), Mmap Latency")
    local_bigger_Prot_Fault = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), Prot Fault")
    local_bigger_Page_Fault = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), Page Fault")
    local_bigger_100fd_selct = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), 100fd selct")
    local_bigger_0K_File_create = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), 0K File create")
    local_bigger_0K_File_delete = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), 0K File delete")
    local_bigger_10K_File_create = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), 10K File create")
    local_bigger_10K_File_delete = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), 10K File delete")
    local_bigger_Pipe = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), Pipe")
    local_bigger_AF_UNIX = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), AF UNIX")
    local_bigger_TCP = models.FloatField(verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), TCP")
    local_bigger_File_reread = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), File reread")
    local_bigger_Mmap_reread = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), Mmap reread")
    local_bigger_Bcopy_libc = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), Bcopy(libc)")
    local_bigger_Bcopy_hand = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), Bcopy(hand)")
    local_bigger_Mem_read = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), Mem read")
    local_bigger_Mem_write = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), Mem write")
    memory_Mhz = models.FloatField(verbose_name="Memory latencies in nanoseconds, Mhz")
    memory_L1 = models.FloatField(verbose_name="Memory latencies in nanoseconds, L1 $")
    memory_L2 = models.FloatField(verbose_name="Memory latencies in nanoseconds, L2 $")
    memory_Main_mem = models.FloatField(verbose_name="Memory latencies in nanoseconds, Main mem")
    memory_Rand_mem = models.FloatField(verbose_name="Memory latencies in nanoseconds, Rand mem")
    test_time = models.DateTimeField(verbose_name="测试时间", default=timezone.now)

    class Meta:
        db_table = 'lmbench'
