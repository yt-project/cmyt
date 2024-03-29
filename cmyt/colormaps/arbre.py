# The "arbre" colormap was originally created by Nathan Goldbaum within the yt-project
import numpy as np

# Used to reconstruct the colormap in viscm
viscm_parameters = {
    "xp": [
        25.813729633909759,
        31.169191027506741,
        -75.940036844432967,
        -15.794085808651431,
        -6.7309972964103792,
    ],
    "yp": [
        14.230225988700568,
        -99.470338983050823,
        9.2867231638418275,
        41.007532956685509,
        31.532485875706215,
    ],
    "min_Jp": 27.2243940579,
    "max_Jp": 94.7771696638,
}

luts = np.transpose(
    (
        [
            0.44131774,
            0.44370177,
            0.44605933,
            0.44839054,
            0.45067478,
            0.45293504,
            0.45516891,
            0.45735977,
            0.45952958,
            0.46167133,
            0.46377662,
            0.4658642,
            0.4679203,
            0.46994924,
            0.4719642,
            0.47394237,
            0.47590549,
            0.47785176,
            0.47976766,
            0.48167637,
            0.48355944,
            0.48542865,
            0.48728952,
            0.48912419,
            0.49095845,
            0.49277134,
            0.49457845,
            0.49637777,
            0.49816203,
            0.49995019,
            0.50171533,
            0.50348733,
            0.50524307,
            0.50700027,
            0.50874826,
            0.51049227,
            0.51223193,
            0.5139633,
            0.51569293,
            0.51741103,
            0.51912775,
            0.52083067,
            0.52253029,
            0.52421475,
            0.52589174,
            0.52755306,
            0.52920041,
            0.53083242,
            0.53244156,
            0.5340366,
            0.53559728,
            0.53714122,
            0.53864625,
            0.54012236,
            0.54156358,
            0.5429568,
            0.54431299,
            0.54561357,
            0.5468594,
            0.54805251,
            0.54917186,
            0.55022123,
            0.55119891,
            0.55208818,
            0.55288205,
            0.55358155,
            0.55417814,
            0.55465144,
            0.55499875,
            0.55521509,
            0.55529007,
            0.55521283,
            0.55496547,
            0.55453915,
            0.55392731,
            0.55311827,
            0.55210037,
            0.55086221,
            0.54939281,
            0.54768186,
            0.54571994,
            0.5434988,
            0.54101159,
            0.53825315,
            0.53522015,
            0.53191138,
            0.52832782,
            0.52447273,
            0.52035171,
            0.51597263,
            0.51134556,
            0.50648253,
            0.5013963,
            0.49610438,
            0.49062382,
            0.48497218,
            0.47916766,
            0.47322878,
            0.46717417,
            0.46102228,
            0.45479123,
            0.44850028,
            0.44216678,
            0.43580508,
            0.42943042,
            0.42305718,
            0.41669888,
            0.41036814,
            0.4040767,
            0.39783545,
            0.39165443,
            0.38554287,
            0.37950919,
            0.37356107,
            0.36770548,
            0.36194865,
            0.35629619,
            0.35075301,
            0.34532345,
            0.34001119,
            0.33481937,
            0.32975052,
            0.32480662,
            0.31998909,
            0.3152988,
            0.31073609,
            0.30630076,
            0.30199208,
            0.29780879,
            0.29374913,
            0.28981083,
            0.28599112,
            0.2822876,
            0.2786961,
            0.27521186,
            0.27183029,
            0.2685464,
            0.26535482,
            0.26224983,
            0.2592254,
            0.25627525,
            0.25339285,
            0.25057146,
            0.24780425,
            0.24508425,
            0.24240456,
            0.23975784,
            0.23713717,
            0.23453574,
            0.23194694,
            0.2293644,
            0.22678204,
            0.22419418,
            0.22159558,
            0.21898153,
            0.21634792,
            0.21369107,
            0.21100766,
            0.2082966,
            0.20555708,
            0.20278935,
            0.19999489,
            0.19717647,
            0.19433834,
            0.19148635,
            0.18862811,
            0.18577317,
            0.18293319,
            0.1801221,
            0.17735631,
            0.17465482,
            0.17203943,
            0.16953482,
            0.16716741,
            0.16496905,
            0.16297318,
            0.16121584,
            0.15973528,
            0.15857143,
            0.15776521,
            0.15735758,
            0.15738856,
            0.15789607,
            0.15891475,
            0.16047487,
            0.16260134,
            0.16531299,
            0.16862212,
            0.17253417,
            0.17704869,
            0.18215934,
            0.1878543,
            0.19411741,
            0.20092909,
            0.20826721,
            0.21610797,
            0.22442667,
            0.23319827,
            0.24239792,
            0.25200153,
            0.26199056,
            0.27233871,
            0.28302468,
            0.29402831,
            0.30533058,
            0.31691362,
            0.3287703,
            0.34087697,
            0.353218,
            0.36577922,
            0.37855287,
            0.39153018,
            0.40469046,
            0.41802196,
            0.43152574,
            0.4451854,
            0.45898439,
            0.47292271,
            0.48699148,
            0.50116973,
            0.51546387,
            0.52985625,
            0.54433284,
            0.55890334,
            0.57353506,
            0.58824263,
            0.60299664,
            0.61780476,
            0.63264342,
            0.64751846,
            0.66240265,
            0.67730956,
            0.69220565,
            0.70709988,
            0.72197277,
            0.73680781,
            0.75161342,
            0.76636275,
            0.78104266,
            0.7956434,
            0.81016108,
            0.82456869,
            0.83884997,
            0.85298622,
            0.8669555,
            0.88073158,
            0.89428251,
            0.90756872,
            0.92054055,
            0.933148,
            0.94530521,
            0.95690622,
            0.96783447,
            0.97790967,
            0.986926,
            0.99464852,
        ],
        [
            0.05626182,
            0.06063603,
            0.06486246,
            0.06895821,
            0.07296132,
            0.0768539,
            0.08064911,
            0.08437114,
            0.08800482,
            0.09156317,
            0.09505774,
            0.09847813,
            0.10183875,
            0.10513951,
            0.1083756,
            0.11156296,
            0.11469159,
            0.11776515,
            0.12079126,
            0.12376178,
            0.12668524,
            0.1295584,
            0.13238112,
            0.13515848,
            0.13788542,
            0.14056641,
            0.14319933,
            0.14578505,
            0.14832396,
            0.15081614,
            0.15326083,
            0.15565984,
            0.15801096,
            0.16031668,
            0.16257524,
            0.16478787,
            0.16695485,
            0.1690751,
            0.17115162,
            0.17318085,
            0.17516841,
            0.1771089,
            0.17900954,
            0.18086473,
            0.18268134,
            0.18445603,
            0.18619262,
            0.18789332,
            0.18955541,
            0.19119063,
            0.19278568,
            0.19436176,
            0.19590425,
            0.19742907,
            0.19893786,
            0.20042606,
            0.20191306,
            0.20339073,
            0.2048706,
            0.20636577,
            0.20786968,
            0.20939933,
            0.21096715,
            0.21257494,
            0.21423423,
            0.21596274,
            0.21777215,
            0.21966954,
            0.22167374,
            0.22380222,
            0.22607063,
            0.22849545,
            0.23109288,
            0.23388218,
            0.23688208,
            0.24011005,
            0.24358302,
            0.24731693,
            0.2513262,
            0.25562329,
            0.26021807,
            0.26511744,
            0.2703248,
            0.27583977,
            0.28165796,
            0.28777089,
            0.29416603,
            0.30082712,
            0.30773447,
            0.3148655,
            0.3221953,
            0.32969733,
            0.33734475,
            0.34510833,
            0.35296022,
            0.36087366,
            0.3688232,
            0.37678504,
            0.38473729,
            0.39266014,
            0.40053592,
            0.40834821,
            0.41608347,
            0.42373148,
            0.43128293,
            0.43873028,
            0.44606759,
            0.45329038,
            0.46039546,
            0.46738076,
            0.47424525,
            0.48098872,
            0.48761174,
            0.49411548,
            0.50050166,
            0.50677243,
            0.51293031,
            0.51897811,
            0.52491887,
            0.53075583,
            0.53649234,
            0.54213187,
            0.54767795,
            0.55313418,
            0.55850412,
            0.56379138,
            0.56899954,
            0.57413213,
            0.57919266,
            0.58418458,
            0.58911129,
            0.59397611,
            0.59878205,
            0.60353246,
            0.60823062,
            0.61287956,
            0.61748225,
            0.62204154,
            0.62656023,
            0.63104102,
            0.63548651,
            0.63989924,
            0.64428164,
            0.64863606,
            0.65296474,
            0.65726983,
            0.66155346,
            0.66581762,
            0.67006415,
            0.67429484,
            0.67851134,
            0.68271522,
            0.68690793,
            0.69109084,
            0.69526517,
            0.69943206,
            0.70359259,
            0.70774778,
            0.7118983,
            0.71604481,
            0.72018788,
            0.72432796,
            0.72846539,
            0.73260037,
            0.73673302,
            0.74086331,
            0.74499111,
            0.7491162,
            0.75323821,
            0.7573567,
            0.76147109,
            0.76558071,
            0.7696848,
            0.77378264,
            0.7778731,
            0.7819551,
            0.78602749,
            0.79008902,
            0.79413838,
            0.79817417,
            0.80219489,
            0.80619902,
            0.81018492,
            0.81415092,
            0.81809528,
            0.82201619,
            0.8259118,
            0.82978021,
            0.83361959,
            0.83742793,
            0.84120311,
            0.84494307,
            0.84864571,
            0.85230891,
            0.85593052,
            0.85950837,
            0.86304028,
            0.86652408,
            0.86995756,
            0.87333854,
            0.87666491,
            0.87993431,
            0.88314454,
            0.88629345,
            0.88937891,
            0.89239883,
            0.89535078,
            0.89823289,
            0.9010432,
            0.9037798,
            0.90644047,
            0.90902303,
            0.91152628,
            0.91394863,
            0.91628739,
            0.91854149,
            0.92071018,
            0.92279108,
            0.92478281,
            0.92668571,
            0.92849682,
            0.93021638,
            0.93184454,
            0.9333779,
            0.93481986,
            0.93616638,
            0.93742098,
            0.9385809,
            0.93964931,
            0.94062391,
            0.94150928,
            0.94230167,
            0.94300773,
            0.9436249,
            0.9441573,
            0.94460885,
            0.94497728,
            0.9452696,
            0.94548972,
            0.94564084,
            0.94572458,
            0.94574964,
            0.94572195,
            0.94564856,
            0.94553784,
            0.94539999,
            0.94524753,
            0.94509613,
            0.94496566,
            0.94487644,
            0.94486297,
            0.94496862,
            0.9452415,
            0.94575723,
            0.94660423,
            0.94788672,
        ],
        [
            0.04951266,
            0.06083219,
            0.07165053,
            0.08210915,
            0.09247329,
            0.10260581,
            0.11257765,
            0.12255122,
            0.13238498,
            0.14215586,
            0.15194141,
            0.16162489,
            0.17131665,
            0.18099838,
            0.19059467,
            0.20026607,
            0.20988044,
            0.21946015,
            0.22909981,
            0.23866289,
            0.24827349,
            0.25786718,
            0.2674192,
            0.27704703,
            0.28660208,
            0.2962198,
            0.30581382,
            0.31540414,
            0.3250423,
            0.33462062,
            0.34430922,
            0.35393291,
            0.36363845,
            0.37332276,
            0.38305586,
            0.39280948,
            0.40258886,
            0.41242099,
            0.42226577,
            0.43218573,
            0.44211511,
            0.45213185,
            0.46216464,
            0.47228627,
            0.48244044,
            0.49267364,
            0.50296577,
            0.51331525,
            0.52375993,
            0.53422779,
            0.54483694,
            0.55545388,
            0.56620423,
            0.57700138,
            0.5878611,
            0.59884035,
            0.60984329,
            0.62095468,
            0.63213636,
            0.6433441,
            0.6546616,
            0.6660279,
            0.67741372,
            0.68886382,
            0.70036612,
            0.71186928,
            0.72336666,
            0.73489587,
            0.74641297,
            0.75788429,
            0.76929516,
            0.7806286,
            0.79188503,
            0.80303085,
            0.81402588,
            0.82484364,
            0.83545535,
            0.84583016,
            0.85593546,
            0.86573722,
            0.87520057,
            0.88429036,
            0.89297186,
            0.90121149,
            0.90897763,
            0.91624135,
            0.92297716,
            0.92916362,
            0.93478393,
            0.93982627,
            0.944284,
            0.9481558,
            0.95144555,
            0.95416177,
            0.95631799,
            0.95793177,
            0.95902407,
            0.95961865,
            0.95974148,
            0.95942014,
            0.95868324,
            0.95756071,
            0.95608217,
            0.9542758,
            0.95216987,
            0.94979177,
            0.94716782,
            0.94432316,
            0.94128162,
            0.93806566,
            0.93469637,
            0.93119344,
            0.92757518,
            0.92385855,
            0.92005924,
            0.91619167,
            0.91226907,
            0.90830358,
            0.90430622,
            0.90028706,
            0.8962552,
            0.89221888,
            0.88818549,
            0.88416167,
            0.88015334,
            0.87616574,
            0.87220349,
            0.86827062,
            0.86437059,
            0.86050638,
            0.85668045,
            0.85289483,
            0.84915193,
            0.84545249,
            0.84179674,
            0.83818509,
            0.83461764,
            0.83109413,
            0.82761399,
            0.82417636,
            0.82078008,
            0.81742372,
            0.81410558,
            0.81082372,
            0.80757594,
            0.80435989,
            0.80117258,
            0.79801115,
            0.79487252,
            0.79175341,
            0.78865036,
            0.78555973,
            0.78247771,
            0.77940035,
            0.77632353,
            0.77324301,
            0.77015423,
            0.76705215,
            0.76393282,
            0.76079161,
            0.75762382,
            0.75442468,
            0.7511894,
            0.74791315,
            0.74459109,
            0.74121838,
            0.73779019,
            0.73430173,
            0.73074825,
            0.72712503,
            0.72342746,
            0.71965096,
            0.71579107,
            0.71184237,
            0.70780168,
            0.70366489,
            0.69942802,
            0.69508722,
            0.69063878,
            0.68607916,
            0.68140497,
            0.67661297,
            0.67170012,
            0.66666354,
            0.66150054,
            0.65620859,
            0.65078539,
            0.64522878,
            0.63953554,
            0.63370386,
            0.62773308,
            0.62162183,
            0.61536895,
            0.60897349,
            0.60243471,
            0.59575208,
            0.5889253,
            0.58195428,
            0.57483914,
            0.56757997,
            0.56016891,
            0.55261464,
            0.54491821,
            0.53708088,
            0.52910417,
            0.52098984,
            0.51272693,
            0.50432884,
            0.49579898,
            0.48714013,
            0.47834844,
            0.46942272,
            0.46037716,
            0.45121575,
            0.4419283,
            0.43252618,
            0.42302131,
            0.41340722,
            0.40368844,
            0.3938839,
            0.38398203,
            0.37399931,
            0.36394886,
            0.35381793,
            0.34364247,
            0.33340639,
            0.32314442,
            0.31285132,
            0.30255889,
            0.2922684,
            0.28202116,
            0.27181653,
            0.26171116,
            0.25171982,
            0.24189603,
            0.23229831,
            0.22296839,
            0.21399898,
            0.20548226,
            0.19752366,
            0.19024226,
            0.18379968,
            0.17836522,
            0.17412601,
            0.17128095,
            0.17003118,
            0.17056788,
            0.17305931,
            0.17763999,
            0.18441057,
            0.19343386,
            0.2047358,
            0.21833687,
            0.2341978,
            0.25223614,
            0.2722682,
        ],
    )
)
