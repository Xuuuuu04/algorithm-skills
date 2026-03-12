# cangjie_libbpf

cangjie libbpf bindings

## Supported API

* cj_libbpf_major_version
* cj_libbpf_minor_version
* cj_libbpf_version_string

* cj_bpf_object__open
* cj_bpf_object__close
* cj_bpf_object__load
* cj_bpf_object__find_program_by_name
* cj_bpf_object__find_map_by_name
* cj_bpf_object__pin_maps
* cj_bpf_object__unpin_maps
* cj_bpf_object__pin_programs
* cj_bpf_object__unpin_programs
* cj_bpf_object__pin
* cj_bpf_object__unpin

* cj_bpf_obj_pin
* cj_bpf_obj_pin_opts

* cj_bpf_xdp_attach
* cj_bpf_xdp_detach

* cj_bpf_map__update_elem
* cj_bpf_map__lookup_elem
* cj_bpf_map__delete_elem
* cj_bpf_map__get_next_key
* cj_bpf_map__set_pin_path
* cj_bpf_map__pin_path
* cj_bpf_map__is_pinned
* cj_bpf_map__pin
* cj_bpf_map__unpin
* cj_bpf_map__fd

* cj_bpf_program__fd
* cj_bpf_program__attach
* cj_bpf_program__attach_uprobe_opts
* cj_bpf_program__attach_usdt
* cj_bpf_program__attach_cgroup
* cj_bpf_program__pin
* cj_bpf_program__unpin

* cj_bpf_link__destroy
* cj_bpf_link__pin_path
* cj_bpf_link__pin
* cj_bpf_link__unpin

* cj_bpf_tc_hook_create
* cj_bpf_tc_hook_destroy
* cj_bpf_tc_attach
* cj_bpf_tc_detach

* cj_perf_buffer__new
* cj_perf_buffer__free
* cj_perf_buffer__poll

* cj_ring_buffer__new
* cj_ring_buffer__free
* cj_ring_buffer__poll

## Example

XDP

https://gitcode.com/hevienz/cangjie_libbpf_xdp_example

Uprobe

https://gitcode.com/hevienz/cangjie_libbpf_uprobe_example

TC

https://gitcode.com/hevienz/cangjie_libbpf_tc_example

Kprobe

https://gitcode.com/hevienz/cangjie_libbpf_kprobe_example

Tracepoint

https://gitcode.com/hevienz/cangjie_libbpf_tracepoint_example

USDT

https://gitcode.com/hevienz/cangjie_libbpf_usdt_example

CGroup SKB

https://gitcode.com/hevienz/cangjie_libbpf_cgroup_skb_example

## Related Projects

pysonar4cj

https://gitcode.com/hevienz/pysonar4cj

