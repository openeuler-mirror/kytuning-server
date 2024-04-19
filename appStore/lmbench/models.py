from django.db import models
import django.utils.timezone as timezone


# Create your models here.
class Lmbench(models.Model):
    """Lmbench表"""
    env_id = models.IntegerField(verbose_name='环境id')
    execute_cmd = models.CharField( max_length=255, verbose_name='执行命令',null=True,blank=True)
    modify_parameters = models.CharField(max_length=255, verbose_name='修改参数',null=True,blank=True)
    basic_Mhz = models.FloatField(verbose_name="Basic system parameters, Mhz",null=True,blank=True)
    basic_tlb_pages = models.FloatField(verbose_name="Basic system parameters, tlb pages",null=True,blank=True)
    basic_cache_line_bytes = models.FloatField(verbose_name="Basic system parameters, cache line bytes",null=True,blank=True)
    basic_mem_par = models.FloatField(verbose_name="Basic system parameters, mem par",null=True,blank=True)
    basic_scal_load = models.FloatField(verbose_name="Basic system parameters, scal load",null=True,blank=True)
    processor_null_call = models.FloatField(verbose_name="Processor, null call",null=True,blank=True)
    processor_null_I_O = models.FloatField(verbose_name="Processor, null I/O",null=True,blank=True)
    processor_stat = models.FloatField(verbose_name="Processor, stat",null=True,blank=True)
    processor_open_clo = models.FloatField(verbose_name="Processor, open clo",null=True,blank=True)
    processor_slct_TCP = models.FloatField(verbose_name="Processor, slct TCP",null=True,blank=True)
    processor_sig_inst = models.FloatField(verbose_name="Processor, sig inst",null=True,blank=True)
    processor_sig_hndl = models.FloatField(verbose_name="Processor, sig hndl",null=True,blank=True)
    processor_fork_proc = models.FloatField(verbose_name="Processor, fork proc",null=True,blank=True)
    processor_exec_proc = models.FloatField(verbose_name="Processor, exec proc",null=True,blank=True)
    processor_sh_proc = models.FloatField(verbose_name="Processor, sh proc",null=True,blank=True)
    processor_Mhz = models.FloatField(verbose_name="Processor, Mhz",null=True,blank=True)
    basic_intgr_bit = models.FloatField(verbose_name="Basic integer operations, intgr bit",null=True,blank=True)
    basic_intgr_add = models.FloatField(verbose_name="Basic integer operations, intgr add",null=True,blank=True)
    basic_intgr_mul = models.FloatField(verbose_name="Basic integer operations, intgr mul",null=True,blank=True)
    basic_intgr_div = models.FloatField(verbose_name="Basic integer operations, intgr div",null=True,blank=True)
    basic_intgr_mod = models.FloatField(verbose_name="Basic integer operations, intgr mod",null=True,blank=True)
    basic_int64_bit = models.FloatField(verbose_name="Basic integer operations, int64 bit",null=True,blank=True)
    basic_int64_add = models.FloatField(verbose_name="Basic integer operations, int64 add",null=True,blank=True)
    basic_int64_mul = models.FloatField(verbose_name="Basic integer operations, int64 mul",null=True,blank=True)
    basic_int64_div = models.FloatField(verbose_name="Basic integer operations, int64 div",null=True,blank=True)
    basic_int64_mod = models.FloatField(verbose_name="Basic integer operations, int64 mod",null=True,blank=True)
    basic_float_add = models.FloatField(verbose_name="Basic float operations, float add",null=True,blank=True)
    basic_float_mul = models.FloatField(verbose_name="Basic float operations, float mul",null=True,blank=True)
    basic_float_div = models.FloatField(verbose_name="Basic float operations, float div",null=True,blank=True)
    basic_float_bogo = models.FloatField(verbose_name="Basic float operations, float bogo",null=True,blank=True)
    basic_double_add = models.FloatField(verbose_name="Basic double operations, double add",null=True,blank=True)
    basic_double_mul = models.FloatField(verbose_name="Basic double operations, double mul",null=True,blank=True)
    basic_double_div = models.FloatField(verbose_name="Basic double operations, double div",null=True,blank=True)
    basic_double_bogo = models.FloatField(verbose_name="Basic double operations, double bogo",null=True,blank=True)
    context_2p_0K = models.FloatField(verbose_name="Context switching, 2p/0K",null=True,blank=True)
    context_2p_16K = models.FloatField(verbose_name="Context switching, 2p/16K",null=True,blank=True)
    context_2p_64K = models.FloatField(verbose_name="Context switching, 2p/64K",null=True,blank=True)
    context_8p_16K = models.FloatField(verbose_name="Context switching, 8p/16K",null=True,blank=True)
    context_8p_64K = models.FloatField(verbose_name="Context switching, 8p/64K",null=True,blank=True)
    context_16p_16K = models.FloatField(verbose_name="Context switching, 16p/16K",null=True,blank=True)
    context_16p_64K = models.FloatField(verbose_name="Context switching, 16p/64K",null=True,blank=True)
    local_2p_0K = models.FloatField(verbose_name="*Local* Communication latencies, 2p/0K",null=True,blank=True)
    local_Pipe = models.FloatField(verbose_name="*Local* Communication latencies, Pipe",null=True,blank=True)
    local_AF_UNIX = models.FloatField(verbose_name="*Local* Communication latencies, AF UNIX",null=True,blank=True)
    local_UDP = models.FloatField(verbose_name="*Local* Communication latencies, UDP",null=True,blank=True)
    local_TCP = models.FloatField(verbose_name="*Local* Communication latencies, TCP",null=True,blank=True)
    local_TCP_conn = models.FloatField(verbose_name="*Local* Communication latencies, TCP conn",null=True,blank=True)
    local_RPC_TCP = models.FloatField(verbose_name="*Local* Communication latencies, RPC/TCP",null=True,blank=True)
    local_RPC_UDP = models.FloatField(verbose_name="*Local* Communication latencies, RPC/UDP",null=True,blank=True)
    local_bigger_Mmap_Latency = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), Mmap Latency",null=True,blank=True)
    local_bigger_Prot_Fault = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), Prot Fault",null=True,blank=True)
    local_bigger_Page_Fault = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), Page Fault",null=True,blank=True)
    local_bigger_100fd_selct = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), 100fd selct",null=True,blank=True)
    local_bigger_0K_File_create = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), 0K File create",null=True,blank=True)
    local_bigger_0K_File_delete = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), 0K File delete",null=True,blank=True)
    local_bigger_10K_File_create = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), 10K File create",null=True,blank=True)
    local_bigger_10K_File_delete = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), 10K File delete",null=True,blank=True)
    local_bigger_Pipe = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), Pipe",null=True,blank=True)
    local_bigger_AF_UNIX = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), AF UNIX",null=True,blank=True)
    local_bigger_TCP = models.FloatField(verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), TCP",null=True,blank=True)
    local_bigger_File_reread = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), File reread",null=True,blank=True)
    local_bigger_Mmap_reread = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), Mmap reread",null=True,blank=True)
    local_bigger_Bcopy_libc = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), Bcopy(libc)",null=True,blank=True)
    local_bigger_Bcopy_hand = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), Bcopy(hand)",null=True,blank=True)
    local_bigger_Mem_read = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), Mem read",null=True,blank=True)
    local_bigger_Mem_write = models.FloatField(
        verbose_name="*Local* Communication bandwidths in MB/s(Bigger is better), Mem write",null=True,blank=True)
    memory_Mhz = models.FloatField(verbose_name="Memory latencies in nanoseconds, Mhz",null=True,blank=True)
    memory_L1 = models.FloatField(verbose_name="Memory latencies in nanoseconds, L1 $",null=True,blank=True)
    memory_L2 = models.FloatField(verbose_name="Memory latencies in nanoseconds, L2 $",null=True,blank=True)
    memory_Main_mem = models.FloatField(verbose_name="Memory latencies in nanoseconds, Main mem",null=True,blank=True)
    memory_Rand_mem = models.FloatField(verbose_name="Memory latencies in nanoseconds, Rand mem",null=True,blank=True)
    test_time = models.DateTimeField(verbose_name="测试时间", default=timezone.now)

    class Meta:
        db_table = 'lmbench'
