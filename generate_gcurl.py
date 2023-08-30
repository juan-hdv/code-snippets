import sys
import re

"""
    Find all the ocurrences of the <pattern> (RegExp) on the file <filename> 
    and print one line with a gcurl call using each ocurrence
"""


def main():
    filename = sys.argv[1]
    pattern = sys.argv[2]

    with open(filename, "r") as f:
        data = f.read()

    pattern = re.compile(rf"{pattern}")
    for reference_id in re.findall(pattern, data):
        s = (
            'grpcurl -plaintext -d \'{ "reference_id": '
            + f'"{reference_id}", '
            + '"verification": "", "tst_context": "{\\"use_fake_providers\\":true}" }\'  -proto silent_verify_proto/ts/proto/silent_verify/v1/silent_verify.proto --import-path silent_verify_proto 0.0.0.0:5001  ts.proto.silent_verify.v1.SilentVerifyService/Finalize'
        )
        print(s)


if __name__ == "__main__":
    main()
