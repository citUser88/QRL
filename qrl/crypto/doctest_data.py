# coding=utf-8
# Distributed under the MIT software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php.

xmss_test_seed1 = '0'*48
xmss_test_seed2 = '31'*24

new_keys_expected = ('000000000000000000000000000000000000000000000000', '\x83\xa9\x1aMzV\n\xbdA\xea\x95\xf4\x12\xcd\xe9\x8e\xda\x03v\x9dr\xb5u[\xb7\xc4\xabt3\xe750 ?\xa6p\xa4\xc6\xd4\xf2\xadZ\xc0\xf8\xf0\xce0\xa7', "2\xee\xe8\x08\xdc|]\xfe&\xfdHY\xb4\x15\xe5\xa7\x13\xbdv@6\xbb\xee\xfdzT\x1d\xa9\xa1\xcc{\x9f\xca\xf1}\xa09\xa6'V\xb685\xde\x17i\xe0^")

xmss_pk_expected1 = '26b3bcc104d686ecfd9fdea7b1963384339121430fbe056cab7c3048ea3e4c4e51ec21420dd061739e4637fd74517a46f86f89e0fb83f2526fafafe356e564ff'

xmss_pk_expected2 = 'ad904af119d215bdc8eeba2cad0c4016e65a180fbe3f6a13589db5d395eef773df2355c48096f2351e4d04db57b326c355345552d31b75a65ac18b1f6d7c7875'

xmss_sk_expected1 = '000000005f2eb95ccf6a0e3e7f472c32d234340c20b3fd379dc28b710affcc0cb2afa57b3aa40c0f99459afe7efe72eb9517ee8ded49ccd51dab72ebf6bc37d73240bb3a51ec21420dd061739e4637fd74517a46f86f89e0fb83f2526fafafe356e564ff26b3bcc104d686ecfd9fdea7b1963384339121430fbe056cab7c3048ea3e4c4e'

xmss_sk_expected2 = '00000000ad70ef34f316aaadcbf16a64b1b381db731eb53d833745c0d3eaa1e24cf728a221e00f865b3457b6f9a95deff8326d07bbdd59f37feffb06b7fc7e8f881fb36adf2355c48096f2351e4d04db57b326c355345552d31b75a65ac18b1f6d7c7875ad904af119d215bdc8eeba2cad0c4016e65a180fbe3f6a13589db5d395eef773'

xmss_mnemonic_expected1 = 'corps adopt corps adopt corps adopt corps adopt corps adopt corps adopt corps adopt corps adopt corps adopt corps adopt corps adopt corps adopt corps adopt corps adopt corps adopt corps adopt'
xmss_mnemonic_expected2 = 'creepy bear couple creek creepy bear couple creek creepy bear couple creek creepy bear couple creek creepy bear couple creek creepy bear couple creek creepy bear couple creek creepy bear couple creek'
xmss_mnemonic_test1 = 'monies hoarse knee socket dock ladder monk abide child junior gill snack gloss bigger pink air spray ponder horrid tube stack luxury recent vein nicely arrive adam short burst keep bright steer'
xmss_mnemonic_test2 = 'sold okay patrol wright swear egg shrimp dinner baker employ seeing assign share top siege age donkey utter medium dizzy latent fine campus evade bed mental overt squash query wind horse murmur'

xmss_sign_expected1 = '000000001a214b567518ed5e9564784b5727ebf20faa02018db436fa3fc548f0cd5a6385ad8689b5c2b26f94066be2e0d6f084c7b75e8db58a56a5d2bd97597f3b94838aec868b5223910a13633806488a968ab76d4b6a1d29dff5af7c6e6dc8da4333f7fe5b4456c59c7a6bf93489b747c2a2cc24c8ec6756888e84fa9df219eaa4168b570f9618e65c686d33530c11f5275e4cfb604c83088de8f760f02d5ef67ca3d4f438ca95602777e0355af654e186ac74ecfa3287e2eb92ca99139d4badbc3758efd69c3c84af219f7f340f3b2fa3d28dbd1d21b037be4e3a54fe2fae5e7c41def958ed0160765e650679bd0c4f07eea7ec27934ff8738327434269a2cef4f6613ecff06098952e36f6e0bbc679392c8c6656c725c6c66694871276af3e33911ed736137ee9872402382f509f77db45153fe627c17ee392b5ba7a9593d048a71861405fb706929379d9039634ba8fdb0acc19bd6d60dd5f5adf867fe8b68489bb7a20f005c430321f2a858b05048f5cb7cc896186459d0be38a96f5f31423c79fbc037007d08ba9cd4425de2f644e8dafd18199dec224ec023fcb9eb510daaca49f2b79df4efc7f7cc3560aacabbe17bcfc8dae536e3c8450fd5c442b50da52eadeec2b368698714b19451317a65abbb427a875126c7d306d84635d2ba9db3ea8482a78a60d0983c994e207e4854bbc97f8b79257d29cd4a9cda4b2e2522cabf172ad55afa42300b5b449a780f203e5fbbc20b08f5de93d5352d440bc3668e5c0109d400175ae6236012af3549cdf59489ff63a48caae649d35564932026d7f2fcf40b1c5da69e75d5f0c21864c628201189014d40037dcacb48d38068b825c17ec83435701c995e290e71f37bda6c3e8da68528b98c75d8f2b48fcf7fb08cd6c14544daff0afacfdeafb57c38c8c91236155acee4ea99682081c0a24a1426e345552fb30a211c7e3031155aec2ebccbf200c91c74901703b86d3d4461aa5529238f74e952990ec92eda0e1537a456e3e95f704b150dda732e34d39d7c4b954c7d4aa0ef25eb10978cb106a23811b74f36c8665bf5af3f02a1c9c727f81d359ef3be2f697383de0a6e97929eb8a992ee9313bb9cd954e1957e960f37f096696bb05470f3ec116c80c885b44cc1bceefaf7e273b95bf02f3f3973eef294e31f4c75380ff515d85a5d3519f5e9b7cf8d788de0bc3891883e9f24817898b4fcf53beff0ba4cfcebf55c7d6e1d33e077081e8f77d9f8691650648861b722af954a7042d42cc96e455ae9f0ed71e38ea7ccf405ff54a2dba58dfe40c72d41db80ed9b43f753f3e4bfb9d0f23e5dce9ec254259cee9138550ff7696cbcb03a19495c0d3cfefdf4d66596261d7b70eb9f3a0f3489674b5acaed61b4b5c03b714aba1dbd9c37cb5faa4fcdadc4937bdc627c3424f48486ce4ae47f005bb493390dab4df3ca66052693dae794458e2401ba1196464bd6ed67c3a8dd0138223ef87d2de5dadd3409da70577e0628e2e522e08f718223a2d1917033bde934187727bc7c5e77581b31d3352023184ab4a1145186a1119fee986f4cec6feb7312a98398f9ff5d94e240473c5c02e820671c2e2edc4511ca9c45c909d7560c5bc9385e52adfb0cfbec47fbeb546e8192b7acc39843f98433b7d0c54c761d921490ffe76b22df7de2c52837be92950225b354637cdce10ca2f215f949be584e0208a7d5941543f00ce62d18145de257aa4e89ea7e1a7a15485ef0ad21feb141fda8e0b11f284d7fbe52a962b872ee268c04466e52217af05fea5d120af5fad776fc91f7a4ad64ebe05b373e6b6bc9926e93c5963c43243c099f6eb610f0de3b7f363a9c2d787564cec547d6be10c7d985bd287ef4d379aa8cc6c7df4475bc8d7c25bb8ed6a18006f3f725741aba384a01329b3f81d59b2a072d9e1a416e6424e55bbf1662a54a03bc5f3779416cc0261d8a72eabe2e73a161ca4ebe0715ada9ede5206a7f5517db10191036ae820f606fc8c5b49a4544d17bbf838a05acf9f853a7fa38af9749f54d57de25cc192287746c4bf8798523f751106f7a751454cda89bba679620eed54575208526885e8fdade8ba82f46e453fd3d8bbfe47bceeadd9dd2f67017216f027e8471a78f5ae0c2261a29f947aaa5e64cae27c3da6b6071bc0f49312bbb31739aa57e6897a98d7286c393490811a5612bac96d6d421a107128089df8d05b2750c7d00d371b4ec78a05a5292514a6c339fa93c0fdaba9b414017f6c6b73db4c4aaf33cd0df73f201eaf2f95b595f1af19113ce0d491238a97818232b988065482a736e99d8c920938c463765e46ec616e9bd1d7f80826dec6ae9a1ff3564bfa3a575a70405d93646c1b7277d44b4a2191f631792dd583836d29c6e71a04ecddb4629e6e850ba2144b55f5a1f432c1443224714bf9f0300e32147b862af274345b7366b16ff0951260f6b09c2692164e6f585712ee5d6d7bc3fbc306920653d664f9ee375dd31011778c8db963d53a4b0f7cb9f3db9d29f302b2585fa9ca064e60c19c668b757c069e5cf892f7f5e5140b7c4d3cf0dddaff5329e02188325e659e324d6be8a40bca2b0b164dcfbdcaed85872ac974e9cf9c7af3dc3446c25e58ba1e29d8e6653d4d561a1b7b1518f6397f861e04aab012bfbde4623cf7bea437d2e65c979c9b154ac1ad71f4fbf033782ac2fdbd53997936843374d7631dc4c97908ce2d6df63d75eda564c52669a84b6ebb82301d572e0f15744d110cacca683d2d154bbf4f978b6a1c590a74138c95929123d67f0f56da7c65bf6c99e2180d141611e24d602e48a4ef1dbd396437930026e108015b3d8ef13149e6f4ddcbeb3d46cf812d2149de3d5a2a0faf24b882666da4bd455d5b4c2db966744778c0fc21710209fbab82d700eda3374b0b541c796074d5c4dabad32d21f2574bea0f713c44147623caba4b34c0e5a23662bd6c3090d9b67d9349c47a7d79fc246018eb7c3b341c5ab4ed05a5d858a372a344a494208651ec2fa2458b22dc49b1d4c4095c3e8cfda558968baf71511d2b8dea748255d8bf9ed7b534464fb857ba299f648b475b2835812d81fedf94ff3f141e44bc0953369f49e5a68be2b4a616141f7f2965121c64e463bfc741ba8718dad5ca295ecb968ef6021ceb954881997718603ed89cc8b4b6600eb15864b2d7babf6adbbb8405d03760874868570260ac7bab582d6deaa0125a8b50e05230bf61405ec6b1fc7aa61a6d517ec5a48bd9b2ddd0'
xmss_sign_expected1_h = 4

xmss_sign_expected2 = '00000000688affc5a80cdbe2de8f681ed06ad21b2da842e123ee4ac8df2b7c7ca2992b05b5a861167631876064d5f9bcf907f6c4a7a58000481888e037798147c9def1bd5d6f00959a6875805c8dfdf9d7e67c95ef33c6babb7e475986971605479e437caace1bbd1a190f6f37cb0063023b8ca2d540bcfaeb838fd153e7d1e80f2ade89474088218d5f883d1a6e6b197a0ec6deeba4c0502a43467ac2a6e3bb4cec71fdec1dc050a338d7031d1d5e3b8e307a331e80023bdd63bfb7fe6dc7d1d68e6473835a491eab2a4fcd4bd8f60e151b26d035989dbe2d8148a30459c371e955f5692fd6873804637435a39ea28f36bd81b4040cb1a5c4e4cb1c91a43a1e57839f4cd42b56ee903eb4180f73e65706a00856a71708c8ea514993a58faa7001026f0cfd1df70687f853d9b8f46aacba52903bdd717af79385a1e9924589b568f44ef86e4b60cfe80fa9a634b66f12083003045d0b83fd109dcd57d21569f6ae82fafab8f119d665162fe94e0785e2bf32ae4e9146d99e9b26c6f89ae1848220f7819440c3109098201880e04109a7b61b85ea9ef069bc5f522f8ad6f08f77421153da79b5dc9cf5c2cb640124ee4e9c664f04ba19b4fa140ab97eda96db28f6019c89dd8e23f2da0aca066b422425ab204e98d336206eab9bad338266cf97ebbea9b06d1c5f1f547522a1d4e0abe9491af2317ab99c65a004282a86a7d1b6b9965e62066f494eb5afaf6bb2df41422dfadbfab137f4ce65782f42c80ba6622fbe3c203cf60ad54ed92b97cc81132a9e08eb451dbba97382ec5b24f476954f7a112efe7f2e6c8bcda1f4a875dc8c8c08486994b6ad824724c6dbc0f5bb674ac193051a63f8299392816835201edaaaa9da74ad55cbf2e668bf045ed4ccb063a47810bdc7ff13b253963247a895ceac4a9bc19abd45d44e4cec36ff178c559844b9d8c59868be5c684c7fef7f15e23ac4c7988f19a121d2187142f80b8b2ed4e3a37855501ce1292606dbe847d1f32baeed18ee8ea6dee245f6c204879231d11260f75cf569e0049606220260bc495da851e03b9fea66b4af266450ff8a61349d959d53b6f35250816dd28ce9ed787873f5e7c5727c9e6fb4e49d70413c1e1ebd920c7e7fa6e52f51d63ee460b0ae9de6a38e60a52d893e887cd977b4b78c7a1bad8b1e05d90cf770835751be21708ac38c5233c4e90d21a56fe2ca6f78590ff053a27cbea5cbc777c987ee352f9f8b3977ebd2637f52da686a031f848cc551c1772a84a55a274f99d7bb84e0b76b0d1966c22aafaeda0c6f6af6a4e9b2e11a58d0b0a627132410bd2fa0de0cc5c8b7055ce455dcbaf4d75bc665a708e7fe6842f5684a28c1c0cd1746dbc3c7a1acd456d6a0a41ab958a868739637153f5f364f8ef92aa7479524d36b438fb8c4b07e76ecd1f421f135f36007e0df7756646cf97f4e127f979ced63ca7de6ffa7d36d549a65984169351d151f3b415e4964fd0535dcfe859936d172dc2e6380255315199c1893e8a6c7daad9e1647d548cea274fe97d45cd50281ae3cb0095aaaa72f00e74f80f9fa9ad69f4516452e6d032a0f4785570713976027c4fc056fdf84dbd562b29cbbf6c7075f7c0389693addb08e97d63ae864b861c086580f5f61fb8de32f36dd6329b0850160044455a6f77a2c36440b612a899a02e716867af2784460d251ae9de17b511bafa12da8a36094d524d97a48262700d7bcd557c8f903ac814a5a823feace683b1e4a134d47dad5c834e212ee877ce6e174973d4690a24583d68b4d03cf7befc237b4ea991d3d205682b363846cd043b27ea7a345d94daee19b4548df1ae3c89cce001802ccc8c716786fc4557fcd1329bf9b42ec5c24e2a48dfaf3c810be5d458e5a42429e1e2eea993755578c469660896fbc081c3983e5d618f02365f1cb1c1a0a9e45629c73926e0f32b13bdb40563bb3a18b7874d44d7d9994119da1116c4ee11c9cbc85237faa2d4ef78b9d95eb3fec09c8e8644c386bfc735ddf90d90f7274c3045d3d4f17f2fc161d700c1101a30ae721c654bc300275e2c4af0f9917cdc2a12dd50ca3d5f676fe634bea494e13b77269a8c0bf56132a13721504c77481730befeae46b3f60d8721d35ca223ffdd6933ef1fe26083b5a21b5b3bfcddfb1d86f6caf4c133737aaf50b57ed336a32c79af5e3bf1bb8c303ac8ab114db490ff43b126f3008045913032f3ccf9065a1f457ac15b3378bae160908b1d2a2c192a6d27c584cbb21657ee9cf895d3929e811eb6a00584c69bda6748770574ef87744477255f5517ef4475b347fc0385def7504fc6807e5eea26f1995738aff1b34eb1061efa9e00ec84977260957287f9e691f132aa1cd436cb02583e4e1ddfaaadb806bef8eae6ee795c6f96b7841e26a4b44207c69083c45b3e04af53df87432dd2a151daedb97744d6ef7573411db8f397ad35731cc40c40047282dcbf32c11bbbc2652a994beb22840846e20a5d4e7087d3f7c2a539a0c2396dbf9dfe7ac9a18337aeb78441c0c7570a2f6a89edbb38b84730dec30c35d605135d0a63bcacade647a69beb9d680886f56791d5b4811ef90c17059a8d12c7d8499f0c74e5d00d7a393588c0bdaae0f77014f8c678a21b6b00ec1d5f2b9461291fbff880966b8d2375186eae3ea2e2c9eb94cb1632ac306a31f5645ca0cf5022d7dd33901ffc1e21056adc2cb7ad405c23f57836514987ec579ea7910f276dab925fe275cc2e0777ebfc1d17dfae6a1450fb7be3946860b358c7321defa7c4e9eadec3a1059f9a190e1ee48bcc9592e68b0827f946f76d7c654944a085822d95d3b0a096060cf18641faa9a04b1cf88f3aec6f1feeee973447ef7198a2a4970ec8bf7070fffea1d1b4cb009315ee674d372948990993c8ef9482b7ceb037a190ed83bc685386ecf48643f0a6a386f188aea573170737832364b01ca400c61ada16140dd1bbbfaa61054699f7de8c0c8ee9b8e2f6b14945dbda1c01ce1821e3a88ea8df362d72bf48c4713b7ede2051593d764074991e5bb1a82af415caa7be5a148c54dd52b1b1773b922baa1ec04a4ae310f555a2b2c982275f2f77c8de85690ce823f0f422abf70afc8acfc6c74afc7e3a7c2092b99201312577698cf0801bacb7f24c0bee985df6fe32491a3619b959f1bdf3f94913f9025aca7c7d277ea49af96e785f73f7634c9410745b7f3aecb110f35a1568c66b396f036ee8dc080ddcd9892a9fb4524d57d996453b4e6c475'
xmss_sign_expected2_h = 4

hashchain_reveal_expected1 = [(29, 96, 125, 229, 220, 132, 12, 163, 27, 108, 220, 138, 162, 160, 197, 231, 21, 131, 150, 178, 113, 3, 163, 161, 40, 201, 121, 148, 211, 62, 63, 206), (232, 128, 5, 167, 127, 32, 74, 146, 138, 239, 152, 131, 149, 126, 128, 121, 56, 26, 215, 218, 112, 5, 28, 69, 103, 194, 6, 217, 178, 223, 172, 99), (53, 91, 167, 154, 48, 174, 165, 111, 129, 216, 140, 220, 119, 242, 48, 116, 239, 19, 122, 62, 150, 144, 59, 56, 3, 87, 25, 1, 110, 22, 201, 25), (79, 242, 153, 156, 125, 11, 141, 14, 85, 27, 66, 104, 68, 8, 182, 226, 29, 207, 17, 104, 147, 140, 42, 101, 166, 223, 243, 22, 107, 162, 18, 166), (30, 243, 67, 0, 222, 18, 249, 123, 203, 166, 77, 23, 239, 221, 202, 61, 135, 134, 143, 175, 83, 47, 144, 212, 18, 119, 203, 180, 8, 61, 30, 61), (34, 193, 67, 108, 240, 251, 191, 165, 12, 80, 79, 3, 65, 160, 179, 14, 107, 178, 186, 245, 160, 116, 86, 73, 74, 134, 122, 106, 162, 53, 207, 245), (106, 94, 150, 129, 48, 3, 170, 29, 67, 142, 95, 197, 134, 43, 132, 224, 231, 16, 246, 33, 30, 226, 9, 243, 189, 30, 67, 157, 227, 162, 219, 3), (39, 63, 228, 76, 242, 245, 227, 115, 127, 236, 159, 9, 144, 222, 210, 18, 134, 23, 236, 254, 26, 81, 184, 208, 82, 139, 8, 156, 54, 14, 251, 64), (69, 11, 156, 105, 74, 208, 245, 229, 24, 176, 16, 45, 72, 31, 2, 33, 235, 8, 71, 18, 119, 59, 138, 91, 35, 127, 4, 222, 139, 170, 181, 201), (55, 30, 227, 171, 8, 241, 137, 65, 125, 164, 162, 150, 3, 123, 96, 57, 54, 10, 229, 170, 93, 69, 253, 250, 2, 202, 35, 140, 82, 183, 242, 19), (44, 92, 222, 9, 97, 255, 253, 235, 23, 163, 135, 114, 16, 168, 9, 46, 141, 234, 197, 37, 70, 156, 145, 208, 89, 30, 1, 48, 54, 71, 83, 186), (255, 104, 19, 197, 40, 136, 155, 118, 189, 143, 60, 6, 169, 28, 28, 40, 56, 33, 226, 9, 94, 223, 194, 224, 60, 45, 252, 36, 173, 65, 151, 75), (0, 27, 31, 15, 208, 167, 117, 172, 133, 193, 128, 208, 81, 24, 46, 97, 241, 121, 49, 145, 68, 26, 45, 110, 167, 0, 91, 198, 132, 230, 95, 128), (192, 234, 189, 199, 116, 137, 5, 55, 88, 176, 10, 167, 235, 86, 185, 13, 63, 4, 97, 32, 231, 191, 124, 149, 167, 121, 234, 162, 34, 234, 183, 77), (84, 111, 200, 195, 237, 7, 199, 42, 25, 214, 108, 191, 91, 38, 223, 215, 240, 77, 204, 120, 148, 190, 193, 43, 205, 247, 9, 227, 41, 95, 168, 111), (250, 169, 47, 219, 117, 85, 55, 54, 171, 24, 214, 210, 61, 202, 79, 16, 68, 84, 51, 210, 54, 132, 29, 101, 154, 234, 60, 197, 184, 73, 72, 52), (186, 64, 43, 20, 239, 12, 207, 232, 44, 206, 188, 211, 36, 124, 40, 246, 92, 120, 209, 150, 172, 200, 83, 243, 166, 241, 141, 214, 49, 118, 128, 44), (215, 130, 170, 209, 185, 146, 217, 146, 143, 87, 116, 47, 56, 102, 137, 149, 184, 22, 240, 66, 49, 135, 13, 194, 7, 124, 4, 122, 132, 206, 165, 56), (44, 250, 214, 228, 39, 243, 34, 255, 114, 84, 253, 63, 189, 118, 92, 48, 49, 176, 171, 94, 106, 148, 35, 14, 210, 31, 180, 197, 52, 151, 3, 172), (82, 169, 144, 127, 142, 108, 54, 254, 163, 65, 99, 201, 54, 184, 21, 156, 60, 240, 116, 79, 95, 165, 10, 12, 221, 1, 125, 129, 86, 172, 22, 22), (45, 187, 234, 230, 46, 22, 70, 195, 72, 225, 82, 241, 78, 79, 149, 238, 119, 1, 244, 152, 128, 204, 99, 5, 120, 94, 46, 125, 18, 74, 91, 73), (68, 184, 95, 72, 110, 68, 73, 39, 7, 19, 50, 194, 241, 191, 45, 238, 150, 210, 43, 228, 247, 230, 72, 85, 48, 72, 180, 182, 55, 215, 82, 236), (108, 219, 131, 93, 12, 32, 39, 184, 38, 134, 226, 78, 85, 100, 111, 69, 21, 155, 172, 157, 48, 95, 49, 100, 128, 28, 227, 54, 23, 242, 49, 5), (151, 43, 53, 222, 46, 71, 80, 39, 217, 249, 69, 21, 241, 186, 148, 110, 137, 68, 124, 245, 172, 234, 141, 112, 165, 28, 46, 56, 6, 183, 159, 92), (102, 76, 59, 14, 38, 246, 100, 60, 191, 33, 190, 36, 57, 118, 5, 88, 174, 197, 208, 85, 13, 83, 92, 167, 7, 63, 243, 144, 53, 15, 95, 85), (173, 121, 32, 56, 173, 75, 17, 250, 110, 130, 17, 246, 203, 152, 197, 142, 148, 254, 80, 124, 113, 23, 210, 235, 114, 97, 254, 80, 104, 215, 19, 36), (78, 200, 3, 181, 97, 47, 218, 253, 198, 87, 31, 126, 194, 161, 111, 185, 154, 97, 229, 213, 14, 187, 167, 167, 107, 133, 114, 58, 86, 114, 250, 138), (26, 169, 39, 30, 162, 155, 21, 19, 72, 171, 21, 43, 241, 229, 206, 169, 36, 196, 223, 213, 184, 176, 155, 22, 176, 164, 106, 75, 202, 37, 106, 76), (193, 204, 50, 166, 187, 198, 157, 73, 200, 40, 29, 33, 237, 209, 138, 76, 78, 126, 82, 45, 212, 31, 65, 111, 123, 222, 135, 216, 120, 105, 0, 98), (115, 168, 64, 1, 12, 46, 194, 147, 181, 111, 45, 10, 83, 195, 123, 58, 186, 75, 185, 26, 110, 6, 174, 13, 14, 40, 96, 73, 83, 119, 21, 77), (30, 28, 240, 186, 11, 85, 217, 214, 133, 197, 194, 200, 44, 255, 209, 146, 35, 165, 226, 22, 203, 107, 30, 244, 154, 151, 239, 90, 12, 29, 174, 105), (33, 136, 106, 201, 230, 157, 197, 250, 216, 18, 125, 9, 139, 63, 230, 11, 198, 166, 124, 9, 170, 210, 51, 69, 215, 108, 21, 16, 70, 58, 67, 143), (150, 13, 95, 198, 47, 208, 204, 133, 202, 102, 245, 247, 57, 125, 238, 182, 21, 252, 85, 228, 33, 224, 16, 8, 133, 179, 221, 201, 96, 21, 165, 177), (43, 212, 242, 242, 206, 162, 176, 38, 249, 0, 92, 203, 251, 211, 254, 134, 36, 110, 160, 8, 120, 128, 110, 220, 97, 34, 126, 162, 34, 83, 236, 201), (185, 11, 82, 221, 40, 219, 211, 173, 107, 73, 170, 56, 211, 25, 155, 49, 57, 87, 178, 24, 33, 85, 76, 131, 168, 221, 110, 119, 248, 225, 122, 207), (38, 253, 59, 44, 26, 118, 130, 68, 61, 64, 237, 254, 184, 100, 11, 239, 226, 207, 234, 158, 152, 31, 56, 14, 117, 168, 34, 162, 144, 160, 170, 101), (181, 93, 124, 208, 91, 163, 38, 59, 6, 165, 19, 190, 104, 145, 177, 216, 47, 245, 41, 8, 192, 228, 111, 224, 70, 32, 9, 234, 188, 254, 66, 167), (250, 59, 210, 209, 99, 178, 141, 90, 141, 94, 93, 249, 5, 216, 185, 162, 240, 89, 94, 239, 1, 247, 121, 121, 57, 198, 109, 158, 98, 116, 93, 190), (42, 151, 76, 221, 152, 16, 176, 185, 163, 113, 32, 75, 51, 104, 169, 118, 223, 223, 163, 136, 147, 119, 177, 46, 223, 13, 59, 189, 178, 150, 157, 57), (47, 189, 79, 83, 57, 129, 206, 141, 202, 209, 202, 250, 15, 224, 111, 215, 26, 254, 91, 22, 195, 47, 229, 140, 160, 17, 160, 229, 7, 162, 56, 70), (118, 170, 194, 38, 94, 255, 149, 200, 250, 244, 27, 182, 197, 204, 140, 246, 228, 255, 51, 254, 112, 56, 34, 199, 216, 163, 104, 65, 252, 82, 27, 175), (38, 163, 16, 151, 121, 68, 62, 180, 3, 8, 141, 33, 61, 188, 51, 127, 145, 170, 45, 117, 55, 80, 243, 227, 144, 61, 34, 59, 140, 153, 115, 149), (231, 233, 184, 244, 65, 64, 211, 152, 4, 78, 202, 99, 241, 230, 216, 113, 222, 75, 214, 223, 139, 191, 117, 105, 75, 26, 241, 235, 108, 19, 175, 147), (142, 0, 141, 183, 101, 118, 209, 137, 121, 166, 3, 203, 53, 90, 83, 238, 131, 84, 168, 68, 25, 17, 23, 167, 148, 80, 1, 43, 67, 17, 232, 112), (88, 212, 34, 211, 149, 159, 12, 220, 232, 237, 80, 72, 216, 237, 11, 73, 122, 29, 145, 124, 111, 213, 187, 201, 197, 235, 177, 201, 63, 4, 232, 2), (156, 3, 158, 15, 172, 110, 33, 206, 201, 19, 90, 102, 22, 59, 176, 193, 152, 176, 157, 180, 170, 19, 35, 165, 125, 204, 72, 123, 97, 58, 226, 204), (32, 198, 108, 142, 69, 7, 41, 184, 150, 239, 84, 189, 201, 112, 242, 222, 187, 55, 90, 33, 112, 132, 241, 199, 22, 107, 192, 245, 57, 58, 0, 108), (191, 24, 248, 130, 32, 195, 4, 237, 194, 160, 51, 187, 211, 189, 148, 87, 126, 109, 220, 164, 5, 19, 122, 19, 208, 114, 223, 81, 149, 131, 132, 65), (158, 205, 4, 241, 188, 63, 100, 26, 38, 141, 87, 10, 90, 212, 29, 71, 92, 97, 28, 234, 232, 124, 254, 252, 110, 114, 64, 54, 12, 253, 112, 175), (26, 164, 98, 165, 150, 42, 114, 215, 127, 109, 117, 100, 84, 198, 56, 146, 199, 245, 13, 221, 33, 132, 56, 150, 161, 252, 142, 130, 207, 245, 25, 156)]
