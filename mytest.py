from code2flow.engine import code2flow


def test():
    # file = 'code2flow/engine.py'
    file = '/media/vuong/d1Ext4-2/myrepos/code2flow/tests/test_code/js/simple_a_js/simple_a.js'
    code2flow(
        raw_source_paths=file,
        output_file='out.gv'
    )

test()
