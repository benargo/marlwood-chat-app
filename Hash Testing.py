import hashlib
from argon2 import PasswordHasher

def OldMethod(text):
    i = 0
    while True:
        i = i + 1
        text = str(hashlib.sha512(bytes(str(text) + str(i) + 'f8weucrwirun3wurifiwshfkfdsifjisdjfisjfiosjflsjfiljdslkfjllhwifiwfhownowur8o2rn82u8onu328cu482bu82u48b23u89', 'utf8')).hexdigest())
        if i == 128:
            break

    return str(text)

def OldMethodMoreSecure(text, uniqueSalt):
    i = 0
    while True:
        i = i + 1
        text = str(hashlib.sha512(bytes(str(text) + str(i) + str(uniqueSalt) + 'f8weucrwirun3wurifiwshfkfdsifjisdjfisjfiosjflsjfiljdslkfjllhwifiwfhownowur8o2rn82u8onu328cu482bu82u48b23u89', 'utf8')).hexdigest())
        if i == 32768:
            break

    return str(text)

def NewMethod(text, uniqueSalt):
    ph = PasswordHasher()
    i = 0
    while True:
        i = i + 1
        text = ph.hash(text + str(i) + str(uniqueSalt) + " 5a4ca59dbc25dd4735259607b8a178e64b4e93c61cff5625e0905c96b56394e1ca6add5064999663fb3fd9f6d764dd385972998ad351a19337d474442871bf8491eac53a7acdaed769f1d6f003707cbefdc4986b19cd84da5b951bd9bb674f5813f3ad638a1ebdfd1aa4f86dd2a738f1dd25c34cf54b730b737322d58c2b2b479893ca0bad8e8e22911a6ca44ab43997980cac522d86c7b85edd963c0a32b011a2b4a7cc5ac2dd1c22ac7592e18004b138fb4e52231bd1ff9b78fa287c2250178363b0916d07d829b570383c4edbf8d47776feead5dfa7777b5ab3659cf88cc82b7e67c7905ae35728e3e1920e561fec057b6d65f53fcd0733cfa39557d57ddf019ccf06fd2c42cc9a535987be2fb85a7c782c0b1c7d88092cbeedfb39ba2fd9015a9cba37f2783d195b7d64de2ea24e9360635739dca4c25826f26e45ea7a6d5cf9eba483a06ece6dbf25f9074522fb71583d29f5b2ec2c9f4914cdb8b49d5beb8043396db49829167ec89f979b80a0d8eb70cf185e6048359087924e565da0c8e674135fa5b8085b83368c7f5d81d2ceebc731fb062f7f068670c0db12744bbf6830785d81fcfaa9f4b06a4ae0e99a60526346c942b6024cafaef978689dd6d18ac212b7148a39fb3b4124b7bb27b3b3e615798ebbae4c05a43f4908f035448f5cd90167736bc5e7ccb83d81cffaea589dbbe8e7e636ee5f302d7946a2cfa669e6b9b7b0c557be3673f0c3fcabf20f1424a676f3074529c995ae61d897f87c0ae4ac0085d14653004a2c7269d1d89a24ec4ed76e8ce608b4ea7899e4ac18f21ac0e19753d4f6fb207a620d083cd50f0d41227ee804732e66c789b49dd4a61600cc0b2a2cb46ed338ec87ccac0eee7562e534489b2fe27c58aeef983ac5bb0600f0244698d14dfed3fe7c08745a96fd6e717b1dbdf5a058cdac7ee52c792459bc25cf81daecd5c18c3b341567205d07f612d5c8f46d17e7f5256afd747de7e969614e4c9c1699f9e3c56b713993af09126a9a0edf1aceb148989e509e7f155b2971cd99b3025cd89e320b53ad54927f0b3643a90d2acc39812e920d5fa6f21fc4c85e5287c83113eb6a1fe9b2d06ca495928d786e1732cf9023894019a525db741406aa11fdd6ba034d939dab2ee7cad37f0cc777b0a8295feec46d10efcd607df5b1be99d01213d04aafe2ece29b8533897580378eea8ab7821e3912bdeb834a15b6e5f122e5050b09cf078f4322ebe5670b717d32939978cd45a37e1fb4b8e098d3fe7c7f14a4c5170a4ec19807224f870ba217937f1b3bca692fa062d92602d298e491e84f1f2fec81d29c4d9e9b3fafcae6565af74c1f24cc31e8f554395fb486d232b053ca29b90d11972bca63fbc32a9b4f30964a23c82a3483eb8f2b93365a6ca554546113e28d5b391fa5e40437cf4d6b9475412c60b7ad896292d0ce9f3bb70a0b7a8893c30e7ff151709d0f77616b9dfecdf2faf70aa1c514b98abcc8a2a3b493f7490b02e06dec1a44a1b51b4fde365960c4986365d374910d79be5cd1cb36f7f284e51c1d71838b36222b1ba552e19a988614b4d20794c33c881abe7e3ecf20c02073e140e4a8456c5930845d0afdd1cc05d09c8ad4f0fe39eaa57914f445b2879d47ffe5b8b8eeef8953265251af104568c1123a38981757bf280213e65ee4844574570e5ca6d83949a1c9364f1e9545c6aeafc839a2c6da891a3db7c078ef07048179b585a043f8bav,ndck;sjdiohfkjnfskldsoie80hgrjknopd9fsuuosjfodif9ufjsdkpofsd908huoadnskmdpfo90uf8dhujvnlkpoier90u8dhvjnlkspoie9fu08gyfdjlsnkpoweqr9gyhofjndlkepowi9r0tgysjbvknldkjpoer9t0u8ghojnlakdspoewi9q80tu8hgbjuyre8eupi")
        if i == 4:
            break

    return(str(text))

#print(str(OldMethod("Password")))
#print(str(OldMethodMoreSecure("Password", "Alex")))
print(str(NewMethod("Password", "Alex")))