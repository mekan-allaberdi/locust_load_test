import random


POSTING_ID_LIST = [
    "ba5f7603-0582-4f8c-9d2c-189ae7683431",
    "b8a6f4c4-1246-403b-bc6f-7b2ac130025b",
    "ef3a4a8e-6158-4a26-8d60-3ae458761eaf",
    "56cfcf79-5f91-44d4-8dee-5f073e951a7c",
    "d5ba1aa1-be5c-4193-8bb1-f1f562d684fb",
    "dee31906-8b01-42fc-bc36-58ac99cfab61",
]

STAGE_ID_LIST = [
    "lead-new",
    "lead-reached-out",
    "lead-responded",
    "applicant-new",
    "cdc515f2-ce20-4ab5-bee5-9a9858810c34",
    "a827041b-4154-4a24-a4bd-d8621eb8f847",
    "ec77badc-3593-4d3a-aea1-37bce3d7ad9b",
    "a14c90a1-eb09-4df1-ae9a-762de2fd6e78",
    "990e4f22-aa7f-445e-9238-040ab7fa161a",
    "offer",
    "430d6035-9aca-4212-a1cf-893bb356c46e",
]

OWNER_ID_LIST = [
    "0b0ed3db-ce3e-4e84-83d9-51044a551593",
    "19d13c73-d9f2-4bf8-bb3b-e2947df45088",
    "8c08bd20-f9ed-4bec-a985-eba309702f9b",
    "47057a77-ca7b-4bb5-8af6-d84cc7f24d34",
    "edb1a10f-6456-4bff-abbc-c413b3d666f9",
    "26af3c8b-8027-4b35-a5b5-87686dd7b0b2",
    "02f17322-7ff7-43a2-9fe8-d7a2357792c8",
    "056ec4e8-5774-428f-b64c-b7de0191fe30",
    "aeeabd63-650a-4d0e-a54d-ffe600b1614b",
    "67792f21-f842-40ad-b6f6-b21c4b8da44e",
    "67c7e9cc-9eea-4282-846c-2f4650b3217c",
    "5824ecaa-5ec5-4558-8fad-dee9d1f4a813",
    "70506901-a0b8-41b8-b9e8-f1b0d138e316",
    "f845509c-d86d-47ef-9ebc-19b709314b33",
    "b466eb77-5e51-48d2-b077-0b5bb3109def",
    "c837c6eb-7e35-4652-a65a-0b83ff186f45",
    "a9020dae-f404-4e06-9efb-b13d9f435f8c",
    "6b126a19-515a-481a-ab5c-8f48ab8756de",
    "27ebffc6-5c36-4781-afeb-d3e3bd4a8d1c",
    "311dd0e0-5494-4a22-b13f-92672694a6f7",
    "eaee084e-3271-4cdb-b347-9d3fa48cf0e3",
    "32065539-5aa3-438f-9d1c-620940ce8e37",
    "0d75910e-f3a6-4158-95ea-c97fb16062f0",
]


def random_posting():
    return [random.choice(POSTING_ID_LIST)]
