#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:author: FIL - FST - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>_
:date: janvier 2016
:last revised: 2018-01-27
:Fournit :
	 - L_ETUDIANTS = liste d'étudiants
		étudiant = dict('nip' : XXX, 'nom' : XXX, 'prenom' : XXX, 'formation' : XXX, 'groupe' : XXX)
"""

L_ETUDIANTS = [
	{'nip' : '18790266',
	 'nom' : 'USAL',
	 'prenom' : 'ELODIE',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '19293635',
	 'nom' : 'DIOP',
	 'prenom' : 'MARIEME AICHA',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '19953508',
	 'nom' : 'FRID',
	 'prenom' : 'MOHAMED',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '17487906',
	 'nom' : 'PUJOS ',
	 'prenom' : 'ARTHUR',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '13063093',
	 'nom' : 'SASU',
	 'prenom' : 'DANIEL',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '19639996',
	 'nom' : 'BAES',
	 'prenom' : 'YANN',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '10618426',
	 'nom' : 'BOTTE ',
	 'prenom' : 'NICOLAS',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '12301171',
	 'nom' : 'IKUZA MAHIRWE',
	 'prenom' : 'BENITA',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '19362119',
	 'nom' : 'SAAB',
	 'prenom' : 'JAD',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '12595588',
	 'nom' : 'DIOUM ',
	 'prenom' : 'ISSA',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '11901149',
	 'nom' : 'DONG',
	 'prenom' : 'DI',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '18114786',
	 'nom' : 'HOTE',
	 'prenom' : 'VALENTIN',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '11364736',
	 'nom' : 'REMY',
	 'prenom' : 'LAURA',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '14301165',
	 'nom' : 'YON ',
	 'prenom' : 'MATHILDE',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '12259709',
	 'nom' : 'ASLAN ',
	 'prenom' : 'ALI',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '12702751',
	 'nom' : 'BARA',
	 'prenom' : 'ALEXANDRE',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '11259029',
	 'nom' : 'DUVAL ',
	 'prenom' : 'VINCENT',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '18203631',
	 'nom' : 'FARCY ',
	 'prenom' : 'MARION',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '14859949',
	 'nom' : 'PODA',
	 'prenom' : 'SEBASTIEN',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '16601137',
	 'nom' : 'SBAI',
	 'prenom' : 'WISSEM',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '13269369',
	 'nom' : 'TRARI ',
	 'prenom' : 'ASSIA',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '18247574',
	 'nom' : 'VINAI ',
	 'prenom' : 'CAMILLE',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '14120174',
	 'nom' : 'FACQ',
	 'prenom' : 'JEREMY',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '18730511',
	 'nom' : 'SEYE',
	 'prenom' : 'CHEIKH',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '17071362',
	 'nom' : 'WANG',
	 'prenom' : 'MENGZHEN',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '13189199',
	 'nom' : 'BECU',
	 'prenom' : 'MELANIE',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '11567791',
	 'nom' : 'QUENU ',
	 'prenom' : 'MARION',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '13270864',
	 'nom' : 'YAM ',
	 'prenom' : 'CLEMENT',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '11416558',
	 'nom' : 'BAES',
	 'prenom' : 'JEROME',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '17117651',
	 'nom' : 'QUIEF BOUREL ',
	 'prenom' : 'MARGAUX',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '19807904',
	 'nom' : 'BROUX ',
	 'prenom' : 'FLORENT',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '13007717',
	 'nom' : 'HENIN ',
	 'prenom' : 'LOIC',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '16680567',
	 'nom' : 'BURIE ',
	 'prenom' : 'FELIX',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '11517717',
	 'nom' : 'DE LA SAYETTE',
	 'prenom' : 'OLIVIER',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '11076554',
	 'nom' : 'POTIN ',
	 'prenom' : 'CYRIL',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '16664437',
	 'nom' : 'AMARA ',
	 'prenom' : 'IMAD-EDINE',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '17345734',
	 'nom' : 'BURG',
	 'prenom' : 'QUENTIN',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '17248364',
	 'nom' : 'CATTE ',
	 'prenom' : 'LEWIS',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '14119054',
	 'nom' : 'HAVEZ ',
	 'prenom' : 'ANTOINE',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '16067894',
	 'nom' : 'LELEU ',
	 'prenom' : 'JULIEN',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '14749119',
	 'nom' : 'MONS',
	 'prenom' : 'MAXIME',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '13356818',
	 'nom' : 'WATEL ',
	 'prenom' : 'FLORIAN',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '13958054',
	 'nom' : 'BAUX',
	 'prenom' : 'THOMAS',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '11336820',
	 'nom' : 'INEZA RWANDENZI',
	 'prenom' : 'CARINE',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '12732127',
	 'nom' : 'WANG',
	 'prenom' : 'BINHUA',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '12667134',
	 'nom' : 'ISIK',
	 'prenom' : 'YUSUF',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '18599372',
	 'nom' : 'MBENG BIBADG',
	 'prenom' : 'FABIEN',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '18633938',
	 'nom' : 'BARA',
	 'prenom' : 'SALEM',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '17300783',
	 'nom' : 'KORE',
	 'prenom' : 'HENRY-MICHEL',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '19719352',
	 'nom' : 'MADY',
	 'prenom' : 'MEHDI',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '10912590',
	 'nom' : 'KOCH',
	 'prenom' : 'ANDREAS',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '10188955',
	 'nom' : 'KOZAH TCHEKPI',
	 'prenom' : 'BOUWEDEOU',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '11664431',
	 'nom' : 'ODUL',
	 'prenom' : 'CORENTIN',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '19980604',
	 'nom' : 'ABIH',
	 'prenom' : 'SABAH',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '15028713',
	 'nom' : 'DORE',
	 'prenom' : 'SAMUEL',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '10032514',
	 'nom' : 'NINA',
	 'prenom' : 'JEREMIE',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '15576957',
	 'nom' : 'BLOT',
	 'prenom' : 'LOUISE',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '12740579',
	 'nom' : 'KANE',
	 'prenom' : 'AMADOUMOUSSA',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '11285656',
	 'nom' : 'LIMA',
	 'prenom' : 'RUJERIDAVIDSON',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '12968655',
	 'nom' : 'SAAD',
	 'prenom' : 'CAMILLE',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '15690037',
	 'nom' : 'BEAU',
	 'prenom' : 'CORENTIN',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '16359380',
	 'nom' : 'BLAS',
	 'prenom' : 'SIMON',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '14066715',
	 'nom' : 'PERY',
	 'prenom' : 'BASTIEN',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '17223691',
	 'nom' : 'ADOR',
	 'prenom' : 'MAXIME',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '15211493',
	 'nom' : 'DADA',
	 'prenom' : 'AMINE',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '17617332',
	 'nom' : 'LAMY',
	 'prenom' : 'LOIC',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '15813043',
	 'nom' : 'ABOMO NOAH',
	 'prenom' : 'GUY',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '13882227',
	 'nom' : 'AMINA',
	 'prenom' : 'KUZO ANGE',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '12244822',
	 'nom' : 'BILLY',
	 'prenom' : 'AMELIE',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '16419388',
	 'nom' : 'BOANA',
	 'prenom' : 'TIADZAMA',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '15447796',
	 'nom' : 'DURAY',
	 'prenom' : 'DAMIEN',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '18392612',
	 'nom' : 'KREPA',
	 'prenom' : 'PIERRE',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '16047389',
	 'nom' : 'LEROY',
	 'prenom' : 'ETIENNE',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '13940480',
	 'nom' : 'SERRE',
	 'prenom' : 'REMI',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '12516851',
	 'nom' : 'AHMED',
	 'prenom' : 'KHALED',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '14613459',
	 'nom' : 'ALAER',
	 'prenom' : 'MALLAURY',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '16498799',
	 'nom' : 'CAMUS',
	 'prenom' : 'HUGO',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '10009013',
	 'nom' : 'DACKO',
	 'prenom' : 'CHRISTIAN',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '14644018',
	 'nom' : 'DIDDY',
	 'prenom' : 'CHEIKH TJANI',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '12620502',
	 'nom' : 'FLAIS',
	 'prenom' : 'MAXIMILIEN',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '12827137',
	 'nom' : 'LELEU',
	 'prenom' : 'JULIE',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '11530289',
	 'nom' : 'LEROY',
	 'prenom' : 'QUENTIN',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '17003896',
	 'nom' : 'LOUIS',
	 'prenom' : 'CLEMENT',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '16032342',
	 'nom' : 'PETIT',
	 'prenom' : 'THOMAS',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '15398234',
	 'nom' : 'THAON',
	 'prenom' : 'MAXIME',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '13143041',
	 'nom' : 'TOURE',
	 'prenom' : 'MOHAMED',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '10407421',
	 'nom' : 'VOYEZ',
	 'prenom' : 'SIMON',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '16397324',
	 'nom' : 'IRWIN',
	 'prenom' : 'OLIVER',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '14815353',
	 'nom' : 'LAZAR',
	 'prenom' : 'SARAH',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '10587699',
	 'nom' : 'MPOYI',
	 'prenom' : 'JORDAN',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '12534748',
	 'nom' : 'RAHAL',
	 'prenom' : 'LOUIS',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '12373892',
	 'nom' : 'BELLA',
	 'prenom' : 'MOHAMED',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '16576452',
	 'nom' : 'LOZE ',
	 'prenom' : 'ROMUALD',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '11163474',
	 'nom' : 'ADLI ',
	 'prenom' : 'YASSINE',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '16039207',
	 'nom' : 'MAES ',
	 'prenom' : 'PAULINE',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '15100847',
	 'nom' : 'DUGUE',
	 'prenom' : 'SANDY',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '15852033',
	 'nom' : 'WALLE',
	 'prenom' : 'THIBAULT',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '13491674',
	 'nom' : 'KAMAL',
	 'prenom' : 'ABDELLAH',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '17208777',
	 'nom' : 'TAHIR',
	 'prenom' : 'MOHAMED',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '11150222',
	 'nom' : 'TAHIR',
	 'prenom' : 'HOUDA',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '14706322',
	 'nom' : 'AZOUM',
	 'prenom' : 'ABDELWAHID',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '12346839',
	 'nom' : 'DIAS ',
	 'prenom' : 'FLORIAN',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '12854697',
	 'nom' : 'DUBO ',
	 'prenom' : 'LAURENCE',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '16122398',
	 'nom' : 'GOMES',
	 'prenom' : 'BLANCHE',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '13520887',
	 'nom' : 'BLIOT',
	 'prenom' : 'JULES',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '14539720',
	 'nom' : 'DANG ',
	 'prenom' : 'SALIM',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '12959496',
	 'nom' : 'LOUIS',
	 'prenom' : 'CLEMENT',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '17251123',
	 'nom' : 'ALLAW',
	 'prenom' : 'ALI',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '12521115',
	 'nom' : 'CHEN ',
	 'prenom' : 'JIA YIN',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '19829279',
	 'nom' : 'JAKO ',
	 'prenom' : 'AUPHELYE',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '17971112',
	 'nom' : 'KOHDR',
	 'prenom' : 'KHALED',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '17697764',
	 'nom' : 'SAHRI',
	 'prenom' : 'ANAS',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '12077821',
	 'nom' : 'TOURE',
	 'prenom' : 'ABDOULAYE CHERIF',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '19647757',
	 'nom' : 'AYOUB',
	 'prenom' : 'AHMAD',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '16492035',
	 'nom' : 'MALKI',
	 'prenom' : 'Slim',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '13742969',
	 'nom' : 'SACCO',
	 'prenom' : 'ENZO',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '13956735',
	 'nom' : 'CARON',
	 'prenom' : 'SIMON',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '19275252',
	 'nom' : 'CHENG',
	 'prenom' : 'XU',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '17848474',
	 'nom' : 'HATEM',
	 'prenom' : 'BILAL',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '17660859',
	 'nom' : 'MAKOS',
	 'prenom' : 'ALEKSI',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '15391706',
	 'nom' : 'MILON',
	 'prenom' : 'BENJAMIN',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '12989866',
	 'nom' : 'FINOT',
	 'prenom' : 'TIMOTHEE',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '13458942',
	 'nom' : 'OBAME',
	 'prenom' : 'AXEL',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '19362519',
	 'nom' : 'SOETE',
	 'prenom' : 'CEDRIC',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '15382337',
	 'nom' : 'THIAM',
	 'prenom' : 'EL HADJI KEBA',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '18180728',
	 'nom' : 'HENON',
	 'prenom' : 'VALENTIN',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '19365957',
	 'nom' : 'LOPEZ',
	 'prenom' : 'LUCIEN',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '10828444',
	 'nom' : 'NTARE',
	 'prenom' : 'RUGAMBA',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '11201222',
	 'nom' : 'PERON',
	 'prenom' : 'BENJAMIN',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '18295107',
	 'nom' : 'AAZIB',
	 'prenom' : 'MOHAMED',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '19559262',
	 'nom' : 'AJAMI',
	 'prenom' : 'AYMANE',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '17134139',
	 'nom' : 'HARRE',
	 'prenom' : 'BLANDINE',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '13229732',
	 'nom' : 'LEGAY',
	 'prenom' : 'NICOLAS',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '13171514',
	 'nom' : 'NAGET',
	 'prenom' : 'ARTHUR',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '19298116',
	 'nom' : 'BARAS',
	 'prenom' : 'ANTOINE',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '18317620',
	 'nom' : 'GODON',
	 'prenom' : 'MAEVA',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '18546223',
	 'nom' : 'MATTU',
	 'prenom' : 'HIPPOLYTE',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '11732254',
	 'nom' : 'PATTE',
	 'prenom' : 'THIBAUT',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '17748056',
	 'nom' : 'DEMAN',
	 'prenom' : 'NICOLAS',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '15123682',
	 'nom' : 'LECAT',
	 'prenom' : 'FABIEN',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '19269876',
	 'nom' : 'MASSA',
	 'prenom' : 'JEAN JACQUES',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '11474000',
	 'nom' : 'MOEDE',
	 'prenom' : 'AROL',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '19400212',
	 'nom' : 'BOUTE',
	 'prenom' : 'BENJAMIN',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '12349092',
	 'nom' : 'DEVEY',
	 'prenom' : 'JORDAN',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '12859729',
	 'nom' : 'DUPIF',
	 'prenom' : 'BORIS',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '10597347',
	 'nom' : 'GUIOT',
	 'prenom' : 'CLEMENT',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '15041887',
	 'nom' : 'HAGAG',
	 'prenom' : 'MOHAMED',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '16447834',
	 'nom' : 'LUONG',
	 'prenom' : 'TONY',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '10007896',
	 'nom' : 'DELOT',
	 'prenom' : 'CYRIL',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '18127111',
	 'nom' : 'HAIED',
	 'prenom' : 'AYOUB',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '14720087',
	 'nom' : 'KARTI',
	 'prenom' : 'ADENISS',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '18382050',
	 'nom' : 'LAVAL',
	 'prenom' : 'CELESTIN',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '16943975',
	 'nom' : 'LEVET',
	 'prenom' : 'MARINE',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '13192941',
	 'nom' : 'ZAYNI',
	 'prenom' : 'MOHAMAD KARIM',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '11279317',
	 'nom' : 'LUTUN',
	 'prenom' : 'CHARLOTTE',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '16814572',
	 'nom' : 'SAADI',
	 'prenom' : 'HANANE',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '13833048',
	 'nom' : 'ZHANG',
	 'prenom' : 'HAOZHE',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '10177838',
	 'nom' : 'ZONGO',
	 'prenom' : 'JULIEN',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '19987220',
	 'nom' : 'DELOT',
	 'prenom' : 'NICOLAS',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '17123819',
	 'nom' : 'YEBAS-YEBAS',
	 'prenom' : 'BERENGER ABDEL-MARIE',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '19846983',
	 'nom' : 'AJANA',
	 'prenom' : 'RIM',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '11932597',
	 'nom' : 'BOENS',
	 'prenom' : 'QUENTIN',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '15299648',
	 'nom' : 'HENRY',
	 'prenom' : 'CELESTIN',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '11755652',
	 'nom' : 'PETIT',
	 'prenom' : 'MAXENCE',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '14420697',
	 'nom' : 'THIAM',
	 'prenom' : 'MOUSTAFA',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '14286660',
	 'nom' : 'DUPRE',
	 'prenom' : 'HUGO',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '13616627',
	 'nom' : 'JACOB',
	 'prenom' : 'MAXIME',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '12371007',
	 'nom' : 'SALLE',
	 'prenom' : 'JONATHAN',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '19999410',
	 'nom' : 'DUROT',
	 'prenom' : 'ANTHONY',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '10783932',
	 'nom' : 'GARIN',
	 'prenom' : 'MATTHIEU',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '18286099',
	 'nom' : 'HANOT',
	 'prenom' : 'MEHDI',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '11021825',
	 'nom' : 'BOULY',
	 'prenom' : 'HENRY',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '16117264',
	 'nom' : 'DEVOS',
	 'prenom' : 'THIBAUT',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '18291579',
	 'nom' : 'LELEU',
	 'prenom' : 'FLORENT',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '19009310',
	 'nom' : 'LUCAS',
	 'prenom' : 'CLARA',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '11054257',
	 'nom' : 'LUCOT',
	 'prenom' : 'MICHAEL',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '19196863',
	 'nom' : 'MADRE',
	 'prenom' : 'THIBAULT',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '19941017',
	 'nom' : 'GOSSE',
	 'prenom' : 'ANTOINE',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '10688095',
	 'nom' : 'MORIN',
	 'prenom' : 'RAPHAEL',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '17880474',
	 'nom' : 'SILLE',
	 'prenom' : 'AURELIEN',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '15163444',
	 'nom' : 'SOYEZ',
	 'prenom' : 'MAXIME',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '12540693',
	 'nom' : 'CUGNY',
	 'prenom' : 'MATHIEU',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '19248048',
	 'nom' : 'RIVES',
	 'prenom' : 'QUENTIN',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '14581024',
	 'nom' : 'WALLE',
	 'prenom' : 'THEO',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '16043839',
	 'nom' : 'ZAIRI',
	 'prenom' : 'SOFIANE',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '10001189',
	 'nom' : 'DUHEM',
	 'prenom' : 'CLEMENT',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '11022122',
	 'nom' : 'BRASSART',
	 'prenom' : 'LOIC',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '19125237',
	 'nom' : 'DELAMAERE',
	 'prenom' : 'THEO',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '15413028',
	 'nom' : 'CAPITAINE',
	 'prenom' : 'CECILE',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '17193000',
	 'nom' : 'OUBELAID',
	 'prenom' : 'FOUAD',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '11410781',
	 'nom' : 'BOBEVA',
	 'prenom' : 'ANTONIA',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '14522106',
	 'nom' : 'BREUVART',
	 'prenom' : 'AURELIE',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '10120414',
	 'nom' : 'ELJIRARI ',
	 'prenom' : 'SARA',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '18064368',
	 'nom' : 'KACZMAREK ',
	 'prenom' : 'CLEMENT',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '19833089',
	 'nom' : 'BOUCHARAFA ',
	 'prenom' : 'YOUCEF',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '19360668',
	 'nom' : 'BOUKHATEB ',
	 'prenom' : 'FAIROUZ',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '17007353',
	 'nom' : 'RONDEAU ',
	 'prenom' : 'MAIR',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '11582594',
	 'nom' : 'SEKULARAC',
	 'prenom' : 'NIKOLA',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '13769479',
	 'nom' : 'ELAMRANI',
	 'prenom' : 'HATIM',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '18637607',
	 'nom' : 'MOUSSAFIR',
	 'prenom' : 'ABDELALI',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '12574821',
	 'nom' : 'AMEZIAN',
	 'prenom' : 'AMAL',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '18291734',
	 'nom' : 'ARCICASA ',
	 'prenom' : 'JULIEN',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '13413940',
	 'nom' : 'CATTEAU ',
	 'prenom' : 'NICOLAS',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '17762661',
	 'nom' : 'DJAFFAR',
	 'prenom' : 'MEDHI-DINE',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '16592315',
	 'nom' : 'BRASSART',
	 'prenom' : 'FLORIAN',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '10246701',
	 'nom' : 'EL JAAFARI',
	 'prenom' : 'RAHMA',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '16301379',
	 'nom' : 'KAWASAKI',
	 'prenom' : 'YOSHITAKE',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '10297858',
	 'nom' : 'NOTEBAERT',
	 'prenom' : 'CELIA',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '11642861',
	 'nom' : 'BASUYAU ',
	 'prenom' : 'CHRISTIAN',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '17653958',
	 'nom' : 'BUISSART ',
	 'prenom' : 'ROBIN',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '10594929',
	 'nom' : 'FAUCHART ',
	 'prenom' : 'BASTIEN',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '11950038',
	 'nom' : 'PLANCART ',
	 'prenom' : 'DAMIEN',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '17058477',
	 'nom' : 'AHALLAL ',
	 'prenom' : 'ILIAS',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '14030178',
	 'nom' : 'CLERFAYT',
	 'prenom' : 'ERIC',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '13098257',
	 'nom' : 'DELPLACE',
	 'prenom' : 'FLORIAN',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '14284334',
	 'nom' : 'AMIEVA',
	 'prenom' : 'ESTEBAN',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '18173741',
	 'nom' : 'ZAMBRANO',
	 'prenom' : 'JUAN',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '12522048',
	 'nom' : 'HAUSTANT',
	 'prenom' : 'LUC',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '15923788',
	 'nom' : 'TEYSSANDIER ',
	 'prenom' : 'THOMAS',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '10195544',
	 'nom' : 'BEGHMAM',
	 'prenom' : 'MOHAMED',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '11045003',
	 'nom' : 'JOUNIAU',
	 'prenom' : 'JULES',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '12278430',
	 'nom' : 'KHAMMAR',
	 'prenom' : 'AHLAM',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '13041524',
	 'nom' : 'GAKIMA',
	 'prenom' : 'LAURETTA',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '17716964',
	 'nom' : 'PERREAUX',
	 'prenom' : 'BENJAMIN',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '13404980',
	 'nom' : 'MERCHAT',
	 'prenom' : 'FLORENTIN',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '16059289',
	 'nom' : 'OMIETANSKI',
	 'prenom' : 'ALEXIA',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '17322859',
	 'nom' : 'AL-SHAIBANI',
	 'prenom' : 'SUHAIB',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '10324614',
	 'nom' : 'BABA AHMED',
	 'prenom' : 'LOUNES',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '15741131',
	 'nom' : 'LORIDAN',
	 'prenom' : 'LUCIE',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '13007118',
	 'nom' : 'GAILLARD',
	 'prenom' : 'CHARLOTTE',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '16470864',
	 'nom' : 'LALOYAUX',
	 'prenom' : 'NICOLAS',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '14587804',
	 'nom' : 'FARDJAOUI',
	 'prenom' : 'DAHMANE',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '16945766',
	 'nom' : 'LOGGIA',
	 'prenom' : 'YOHAN',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '12716769',
	 'nom' : 'BOUCHAHDANE',
	 'prenom' : 'FARAH',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '11591811',
	 'nom' : 'BOUTRAA',
	 'prenom' : 'REDOUANE',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '17842793',
	 'nom' : 'DJELLALI',
	 'prenom' : 'FARAH',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '12592073',
	 'nom' : 'HAMAMA',
	 'prenom' : 'HAJAR',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '16580461',
	 'nom' : 'MACHTA',
	 'prenom' : 'SARAH',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '15956815',
	 'nom' : 'MENOUAR',
	 'prenom' : 'SAMI',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '13589205',
	 'nom' : 'OSSELAER',
	 'prenom' : 'KEVIN',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '19759825',
	 'nom' : 'CHUFFART',
	 'prenom' : 'BASTIEN',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '14779238',
	 'nom' : 'BEIRNAERT',
	 'prenom' : 'AUBIN',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '14253600',
	 'nom' : 'BOURJA',
	 'prenom' : 'MEHDY',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '12386099',
	 'nom' : 'MHANNAOUI',
	 'prenom' : 'HAMZA',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '19274199',
	 'nom' : 'ABOUBAKER',
	 'prenom' : 'ASSIA',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '15636265',
	 'nom' : 'MAILLARD',
	 'prenom' : 'ELOISE ELIANE',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '17668968',
	 'nom' : 'KNOCKAERT',
	 'prenom' : 'AMAURY',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '13427480',
	 'nom' : 'DIA',
	 'prenom' : 'AMADOU',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '16888526',
	 'nom' : 'NAIT ALI',
	 'prenom' : 'AHMED',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '15841787',
	 'nom' : 'COULIBALY',
	 'prenom' : 'HABIB DAOUD GBON',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '16841757',
	 'nom' : 'DEBRABABT',
	 'prenom' : 'MAXIME',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '10302597',
	 'nom' : 'GHASABIAN',
	 'prenom' : 'TOROS',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '17578846',
	 'nom' : 'MOUAHBA ',
	 'prenom' : 'CINDY',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '17571188',
	 'nom' : 'DJERABA',
	 'prenom' : 'TAKY',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '13714995',
	 'nom' : 'BOUTAB',
	 'prenom' : 'MEHDI',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '19378506',
	 'nom' : 'KOUKEB ',
	 'prenom' : 'SAKINA',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '14503088',
	 'nom' : 'MESSEBE',
	 'prenom' : 'HENOK ADAM',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '18755071',
	 'nom' : 'AL MOBANIN',
	 'prenom' : 'ABEER',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '13842525',
	 'nom' : 'KOUKEB',
	 'prenom' : 'SOFIANE',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '12044824',
	 'nom' : 'BENABBOU',
	 'prenom' : 'SOULEYMAN',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '14966311',
	 'nom' : 'DEBRABANDER',
	 'prenom' : 'GAUTIER',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '11586712',
	 'nom' : 'HOUEIBIB',
	 'prenom' : 'MOHAMED',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '16306977',
	 'nom' : 'PALUMBO',
	 'prenom' : 'LOUIS',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '16342414',
	 'nom' : 'HENNEBERT',
	 'prenom' : 'JADE',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '17435008',
	 'nom' : 'RYCKEBOER',
	 'prenom' : 'ANTHONY',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '13483508',
	 'nom' : 'OULD BOUAMAMA',
	 'prenom' : 'ILYES',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '11909597',
	 'nom' : 'OUAHIB',
	 'prenom' : 'NASSIME',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '15338372',
	 'nom' : 'VANHECKE',
	 'prenom' : 'JULIEN',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '16423474',
	 'nom' : 'ZANDECKI',
	 'prenom' : 'VINCENT',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '10760621',
	 'nom' : 'LIHOUCK',
	 'prenom' : 'CAMILLE',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '14383120',
	 'nom' : 'BELOUCHRANI ',
	 'prenom' : 'NAWAL',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '11004688',
	 'nom' : 'TRIPICCHIO ',
	 'prenom' : 'MARGAUX',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '19921617',
	 'nom' : 'EN-NECHI',
	 'prenom' : 'HAMZA',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '17844061',
	 'nom' : 'RENONCOURT',
	 'prenom' : 'PAUL',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '15949579',
	 'nom' : 'MARESCAUX',
	 'prenom' : 'DYLAN',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '19843571',
	 'nom' : 'DIBOUCHE',
	 'prenom' : 'MYRIAM',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '14644753',
	 'nom' : 'RAMMACH',
	 'prenom' : 'BADR',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '16871774',
	 'nom' : 'VERWICHT',
	 'prenom' : 'LUCAS',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '17535996',
	 'nom' : 'BERNICHI',
	 'prenom' : 'DOUAA',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '10361731',
	 'nom' : 'VANHECKE',
	 'prenom' : 'JULIEN',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '14385553',
	 'nom' : 'DIBOUCHE',
	 'prenom' : 'OMAR',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '13251329',
	 'nom' : 'SMAKIC',
	 'prenom' : 'ELDIN',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '18975326',
	 'nom' : 'DELBECQUE',
	 'prenom' : 'FABIEN',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '19243029',
	 'nom' : 'PAU',
	 'prenom' : 'CHARLELIE',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '10643730',
	 'nom' : 'LAHRACH',
	 'prenom' : 'ILIAS',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '18263186',
	 'nom' : 'LIMBACH',
	 'prenom' : 'NOE',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '10815370',
	 'nom' : 'GIRAUDET',
	 'prenom' : 'PAUL',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '12060494',
	 'nom' : 'SCHMID ',
	 'prenom' : 'PHILIPPE',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '16652381',
	 'nom' : 'COLARD ',
	 'prenom' : 'LOUISE',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '15348718',
	 'nom' : 'BENARD',
	 'prenom' : 'ADRIEN',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '18075276',
	 'nom' : 'BENKEDDAD',
	 'prenom' : 'SOUHIL',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '12569838',
	 'nom' : 'LIN',
	 'prenom' : 'DIXUAN',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '19487983',
	 'nom' : 'RENAUD ',
	 'prenom' : 'SOLANGE',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '12314698',
	 'nom' : 'NAHOUDA HANAFFI',
	 'prenom' : 'DALILA',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '16995942',
	 'nom' : 'NGOUADJE KENKO',
	 'prenom' : 'REGIS EMMANUEL',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '13423767',
	 'nom' : 'HADJ-DOUDOU',
	 'prenom' : 'IMAN',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '14206526',
	 'nom' : 'EL AHDAB',
	 'prenom' : 'OMAR',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '11592860',
	 'nom' : 'DELGADO TOLENTINO',
	 'prenom' : 'NILL',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '14698810',
	 'nom' : 'VINGADASSAMY',
	 'prenom' : 'LEO',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '12361705',
	 'nom' : 'BASTIDE',
	 'prenom' : 'CHRISTOPHE',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '17978914',
	 'nom' : 'EBO ADOU',
	 'prenom' : 'GADIS ',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '13886570',
	 'nom' : 'EL HADDADI',
	 'prenom' : 'SOUMAYA',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '19369163',
	 'nom' : 'FERRADJI',
	 'prenom' : 'MOHAMED AMOKEANE',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '17480265',
	 'nom' : 'KASANDA MAKOTO',
	 'prenom' : 'DONFILS         21ects/11,02',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '19912762',
	 'nom' : 'PERARD',
	 'prenom' : 'DAPHNE',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '12742824',
	 'nom' : 'LECARDEZ',
	 'prenom' : 'ADRIEN',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '16283372',
	 'nom' : 'MINARD',
	 'prenom' : 'BENJAMIN',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '11185894',
	 'nom' : 'DEHONDT',
	 'prenom' : 'THOMASNICOLAS',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '18958035',
	 'nom' : 'RENARD',
	 'prenom' : 'THEO',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '15976108',
	 'nom' : 'BAILLEUL',
	 'prenom' : 'AURORE',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '16117896',
	 'nom' : 'DESTEE',
	 'prenom' : 'VALENTIN',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '17657133',
	 'nom' : 'FOUQUERAY',
	 'prenom' : 'MATHILDE',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '11606373',
	 'nom' : 'HANQUEZ',
	 'prenom' : 'ALINE',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '12963601',
	 'nom' : 'KUCHLER',
	 'prenom' : 'ADRIEN',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '13100141',
	 'nom' : 'LASNIER',
	 'prenom' : 'AMAURY',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '17267148',
	 'nom' : 'MACQUET',
	 'prenom' : 'MEGHANE',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '19233090',
	 'nom' : 'BOUCHEZ',
	 'prenom' : 'FRANCOIS',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '19931757',
	 'nom' : 'HOCEDEZ',
	 'prenom' : 'ALEXANDRE',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '14848281',
	 'nom' : 'KENGNE',
	 'prenom' : 'FLORIAN',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '18466971',
	 'nom' : 'MATHIEN',
	 'prenom' : 'CAMILLE',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '19133112',
	 'nom' : 'TIERSEN',
	 'prenom' : 'MAXENCE',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '18426825',
	 'nom' : 'TOUADERA',
	 'prenom' : 'EVARISTE',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '17801215',
	 'nom' : 'VERNIER',
	 'prenom' : 'LUC',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '10012437',
	 'nom' : 'WAEYTENS',
	 'prenom' : 'EMILIE',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '15757728',
	 'nom' : 'COUVREUR',
	 'prenom' : 'BARTHELEMY',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '17233037',
	 'nom' : 'KINGBEDE ',
	 'prenom' : 'WILLIAM',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '17439058',
	 'nom' : 'MASQUELIER',
	 'prenom' : 'ALEXIA',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '18473954',
	 'nom' : 'ALVAREZ',
	 'prenom' : 'KEVIN',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '19297198',
	 'nom' : 'BERTHELOOT',
	 'prenom' : 'CLARA',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '18442290',
	 'nom' : 'GUILBERT ',
	 'prenom' : 'COLINE',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '12427331',
	 'nom' : 'LAIGLE',
	 'prenom' : 'ALEXANDRE',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '19444984',
	 'nom' : 'MERLIER ',
	 'prenom' : 'CHARLES',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '13748022',
	 'nom' : 'ROUSSEAU ',
	 'prenom' : 'FRANCOIS',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '16396975',
	 'nom' : 'SIMONE JUNIOR',
	 'prenom' : 'ANTONIA VIANA',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '18988655',
	 'nom' : 'BOUAYED',
	 'prenom' : 'OUSSAMA',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '19420206',
	 'nom' : 'TAILLENDIER',
	 'prenom' : 'KELIAN',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '17050816',
	 'nom' : 'ZAGABE ',
	 'prenom' : 'ADRIEN',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '18878729',
	 'nom' : 'DELPIERRE ',
	 'prenom' : 'PAULINE',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '14099199',
	 'nom' : 'GREIGE',
	 'prenom' : 'MARC',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '16770640',
	 'nom' : 'KOSCIELNIAK ',
	 'prenom' : 'LOUIS',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '10829141',
	 'nom' : 'DEPRIESTER ',
	 'prenom' : 'LISA',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '10598940',
	 'nom' : 'LIBBRECHT',
	 'prenom' : 'ALEXANDRE',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '19918346',
	 'nom' : 'VEROVE ',
	 'prenom' : 'MARIE',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '13325356',
	 'nom' : 'ATMANE ',
	 'prenom' : 'BILAL',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '18194111',
	 'nom' : 'CRESCENCE ',
	 'prenom' : 'ESTELLE',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '19926991',
	 'nom' : 'DANNEELS',
	 'prenom' : 'SOPHIE',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '12753468',
	 'nom' : 'JIMENEZ ',
	 'prenom' : 'THOMAS',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '18327410',
	 'nom' : 'VANOVERBERGHE ',
	 'prenom' : 'CORENTIN',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '11638726',
	 'nom' : 'DUCHIER DESBIENS ',
	 'prenom' : 'FRANCOIS',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '17503446',
	 'nom' : 'MALAMELLI ',
	 'prenom' : 'MEHDI',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '16107075',
	 'nom' : 'WISNIEWSKI ',
	 'prenom' : 'ALEXIS',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '14912847',
	 'nom' : 'BARISEAU',
	 'prenom' : 'FRANCOIS',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '18793398',
	 'nom' : 'BOUDJEMA',
	 'prenom' : 'MEHDI',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '10000045',
	 'nom' : 'DESBIENS ',
	 'prenom' : 'RICHARD',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '14165330',
	 'nom' : 'GENDREY ',
	 'prenom' : 'DONATIEN',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '12389851',
	 'nom' : 'BAILLEUL',
	 'prenom' : 'AXEL',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '19676756',
	 'nom' : 'PIENNE ',
	 'prenom' : 'LOGAN',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '15275181',
	 'nom' : 'TOURNEUR ',
	 'prenom' : 'ROMAIN',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '14056638',
	 'nom' : 'ALI BEY',
	 'prenom' : 'RAYANE',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '12834167',
	 'nom' : 'COURTECUISSE',
	 'prenom' : 'VINCENT',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '15900609',
	 'nom' : 'BAUDRE',
	 'prenom' : 'GUILLAUME',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '15642959',
	 'nom' : 'PECQUEUR ',
	 'prenom' : 'HUGO',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '11364383',
	 'nom' : 'LEFEVERE ',
	 'prenom' : 'CYPRIEN',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '11247660',
	 'nom' : 'OPSOMER ',
	 'prenom' : 'ANTHONY',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '12748087',
	 'nom' : 'POTTIEZ ',
	 'prenom' : 'AURELIEN',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '10045180',
	 'nom' : 'SAADIEH',
	 'prenom' : 'RAMI',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '11101448',
	 'nom' : 'SEPTIER',
	 'prenom' : 'DYLAN',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '10785925',
	 'nom' : 'BASTIEN',
	 'prenom' : 'DELPHINE',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '13059606',
	 'nom' : 'MASQUELIER',
	 'prenom' : 'MAXIMILIEN',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '10387748',
	 'nom' : 'PELAGE',
	 'prenom' : 'FRANCOIS-XAVIER',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '13766604',
	 'nom' : 'RICQUET',
	 'prenom' : 'FLORENT',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '13001788',
	 'nom' : 'CHARLES',
	 'prenom' : 'JEAN-BENOIT',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '16884871',
	 'nom' : 'COUPLEUX',
	 'prenom' : 'ALEXIS',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '17249367',
	 'nom' : 'CREPIEUX',
	 'prenom' : 'SIMON',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '19881195',
	 'nom' : 'LONGUEPEE',
	 'prenom' : 'ALEXANDRE',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '16159615',
	 'nom' : 'MACHTELINCK',
	 'prenom' : 'KEVIN',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '15778404',
	 'nom' : 'OLIVIER',
	 'prenom' : 'ARTHUR',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '15823981',
	 'nom' : 'SCHULER',
	 'prenom' : 'Louis',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '11157068',
	 'nom' : 'ANDRZEJEWSKI',
	 'prenom' : 'ANTOINE',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '13406221',
	 'nom' : 'BOUACEM',
	 'prenom' : 'YANNIS',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '12487940',
	 'nom' : 'CAMBIEN',
	 'prenom' : 'ADRIEN-MAXIMILIEN',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '14366749',
	 'nom' : 'DILLIES',
	 'prenom' : 'MARTIN',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '11146587',
	 'nom' : 'GOURDEL',
	 'prenom' : 'TIPHAINE',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '11229312',
	 'nom' : 'MOHAMED',
	 'prenom' : 'MOURDAS',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '17540280',
	 'nom' : 'VANDAELE',
	 'prenom' : 'CHARLOTTE',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '12856708',
	 'nom' : 'BACQUET',
	 'prenom' : 'MAXENCE',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '11795337',
	 'nom' : 'CARLIER',
	 'prenom' : 'MAXENCE',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '19968375',
	 'nom' : 'DANGLETERRE',
	 'prenom' : 'THOMAS',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '13318942',
	 'nom' : 'GROSSEMY',
	 'prenom' : 'ROMAIN',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '14908751',
	 'nom' : 'JANSSENS',
	 'prenom' : 'THIBAULT',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '12567498',
	 'nom' : 'LAIGNEL',
	 'prenom' : 'ALLAN',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '13197502',
	 'nom' : 'TRAORE',
	 'prenom' : 'SEKOU',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '14985747',
	 'nom' : 'VIOULES',
	 'prenom' : 'CLEMMY',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '12062734',
	 'nom' : 'DHALLEWYN',
	 'prenom' : 'ARNAUD',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '16409576',
	 'nom' : 'BOUGUERRA',
	 'prenom' : 'NAZIM',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '17415067',
	 'nom' : 'DANGREMONT',
	 'prenom' : 'ADRIEN',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '12076859',
	 'nom' : 'DELOBEL',
	 'prenom' : 'OLIVIER',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '11167828',
	 'nom' : 'SERIZEL',
	 'prenom' : 'GABRIELLE',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '13420048',
	 'nom' : 'LOLLIER',
	 'prenom' : 'GUILLAUME',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '16508746',
	 'nom' : 'MOHAMED ABDOULKADER',
	 'prenom' : 'AMAL',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '19006655',
	 'nom' : 'MORTREUX',
	 'prenom' : 'CYRIL',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '13385806',
	 'nom' : 'BAYSIEU',
	 'prenom' : 'TONY',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '13922852',
	 'nom' : 'LONGUET',
	 'prenom' : 'VIVIEN',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '19571974',
	 'nom' : 'MOHAMED FETI',
	 'prenom' : 'NASREEN',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '11825469',
	 'nom' : 'REGHEERE',
	 'prenom' : 'TIMOTHE',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '11858563',
	 'nom' : 'TIERSEN',
	 'prenom' : 'MAXENCE',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '14014814',
	 'nom' : 'DOURNEL',
	 'prenom' : 'AMAURY',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '18215572',
	 'nom' : 'RICQUE',
	 'prenom' : 'FABIEN',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '14839805',
	 'nom' : 'BUDNIEWSKI',
	 'prenom' : 'FLORIAN',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '19861995',
	 'nom' : 'LE BRETON',
	 'prenom' : 'MARINE',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '14642180',
	 'nom' : 'VAN DEN BERGE',
	 'prenom' : 'MANON',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '13048698',
	 'nom' : 'LONGUEPEE',
	 'prenom' : 'LEA',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '14832980',
	 'nom' : 'AUBREE',
	 'prenom' : 'ALEXIS',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '12015998',
	 'nom' : 'BIRRIEN DE BURGHGRAEVE',
	 'prenom' : 'TIMOTHEE',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '18835997',
	 'nom' : 'DELOBELLE TOUSSAINT',
	 'prenom' : 'MATTHIEU',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '15482631',
	 'nom' : 'WATINE',
	 'prenom' : 'JEAN-BAPTISTE',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '15390718',
	 'nom' : 'BRICHE',
	 'prenom' : 'MAXENT',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '14827992',
	 'nom' : 'CHARPENTIER',
	 'prenom' : 'CYRIL',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '14299377',
	 'nom' : 'DESOTEUX',
	 'prenom' : 'MAEL',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '19705317',
	 'nom' : 'BOUSSENA',
	 'prenom' : 'OUSSAMA',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '19972555',
	 'nom' : 'ABOULFATH',
	 'prenom' : 'AHMED',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '12395747',
	 'nom' : 'KHELIFI',
	 'prenom' : 'MOHAMED',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '18904051',
	 'nom' : 'WONG FAT',
	 'prenom' : 'TIMOTHEE',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '14147167',
	 'nom' : 'SEM',
	 'prenom' : 'GUILLAUME',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '11321337',
	 'nom' : 'AKUE GEDU ',
	 'prenom' : 'XAVIER',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '16857010',
	 'nom' : 'HOLUIGUE',
	 'prenom' : 'HATICE',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '18438418',
	 'nom' : 'DE HAGEN',
	 'prenom' : 'GUILLAUME',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '18654941',
	 'nom' : 'TIBERGHIEN ',
	 'prenom' : 'GAETAN',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '19433642',
	 'nom' : 'SAUVAGE',
	 'prenom' : 'PIERRE',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '11348917',
	 'nom' : 'TURKOGLU ',
	 'prenom' : 'TUNCAY',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '12949530',
	 'nom' : 'RODRIGUEZ BALLIEU',
	 'prenom' : 'KEVIN',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '18747136',
	 'nom' : 'LOVERGNE',
	 'prenom' : 'BENJAMIN',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '19348871',
	 'nom' : 'OTOUNGA LIPILA',
	 'prenom' : 'HARMONIE',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '14581692',
	 'nom' : 'TERTAG',
	 'prenom' : 'REYANNE',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '17052995',
	 'nom' : 'ESSALHI',
	 'prenom' : 'MOHAMED ILIAS',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '16996419',
	 'nom' : 'HAULKHORY',
	 'prenom' : 'YASHEEL',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '16989473',
	 'nom' : 'ERRACHIDI ',
	 'prenom' : 'BRAHIM',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '14815044',
	 'nom' : 'MENSAH ATTOH',
	 'prenom' : 'LARISSE',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '14651753',
	 'nom' : 'BAUDCHON ',
	 'prenom' : 'ANTHONY',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '10461057',
	 'nom' : 'BEAUCHAMP',
	 'prenom' : 'GUILLAUME',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '10792026',
	 'nom' : 'SENECHAL ',
	 'prenom' : 'ERWAN',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '19341160',
	 'nom' : 'BARICH',
	 'prenom' : 'HAMZA',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '12028263',
	 'nom' : 'BINTCHA ',
	 'prenom' : 'PATRICK',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '10591162',
	 'nom' : 'MAOUCHA',
	 'prenom' : 'YANIS',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '15801319',
	 'nom' : 'COURCHELLE',
	 'prenom' : 'ROMAIN',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '16979836',
	 'nom' : 'GUELAH',
	 'prenom' : 'SHAHIL',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '11847273',
	 'nom' : 'MESKEH',
	 'prenom' : 'SAMI',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '15045399',
	 'nom' : 'ELBACHRA',
	 'prenom' : 'MOHAMED',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '17022284',
	 'nom' : 'HAOUCHINE',
	 'prenom' : 'HAMZA',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '14604205',
	 'nom' : 'MENSAH AKOVI',
	 'prenom' : 'GHISLAIN STEVE',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '18347800',
	 'nom' : 'HE',
	 'prenom' : 'ZHIJIE',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '13151587',
	 'nom' : 'GIL',
	 'prenom' : 'HUGO',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '19745535',
	 'nom' : 'PREUDHOMME-BONTOUX',
	 'prenom' : 'GEOFFREY',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '13078857',
	 'nom' : 'CAILLIERET',
	 'prenom' : 'THIBAULT',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '16589621',
	 'nom' : 'LORGNIER',
	 'prenom' : 'LILIEN',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '11811741',
	 'nom' : 'EZZAHI',
	 'prenom' : 'LOUBNA',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '17966136',
	 'nom' : 'GHAZLI',
	 'prenom' : 'ASMAA',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '12345111',
	 'nom' : 'ZAKARIA',
	 'prenom' : 'ALEXANDRE',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '14070808',
	 'nom' : 'GERVOIS ',
	 'prenom' : 'XAVIER',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '11582377',
	 'nom' : 'MARZLIN ',
	 'prenom' : 'THIBAULT',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '11001167',
	 'nom' : 'PORTOIS ',
	 'prenom' : 'EDOUARD',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '12751724',
	 'nom' : 'SEYDLITZ ',
	 'prenom' : 'HALVARD',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '10516005',
	 'nom' : 'ALAOUI ISMAILI ',
	 'prenom' : 'LINA              ',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '14086624',
	 'nom' : 'CUVELIER',
	 'prenom' : 'QUENTIN',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '12222651',
	 'nom' : 'HURBAIN ',
	 'prenom' : 'JULIEN',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '10462676',
	 'nom' : 'NZONZI ',
	 'prenom' : 'LORENZO',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '15137685',
	 'nom' : 'TAMIMI ',
	 'prenom' : 'ISMAIL',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '10236699',
	 'nom' : 'ZENATI ',
	 'prenom' : 'LAMINE',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '18003533',
	 'nom' : 'FONTAINE ',
	 'prenom' : 'MALLAURY',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '17597234',
	 'nom' : 'KOMINIARZ ',
	 'prenom' : 'ANAIS',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '16845017',
	 'nom' : 'VERGRIETE ',
	 'prenom' : 'FLORIAN',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '14019808',
	 'nom' : 'DELSOIR ',
	 'prenom' : 'PAULINE',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '17904219',
	 'nom' : 'BALOKI',
	 'prenom' : 'PRISCA',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '10413220',
	 'nom' : 'BOUBZIZ',
	 'prenom' : 'CAMEL',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '19362698',
	 'nom' : 'DESPRINGRE ',
	 'prenom' : 'RAPHAEL',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '18302138',
	 'nom' : 'MONVOISIN',
	 'prenom' : 'PAUL',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '12739956',
	 'nom' : 'LHERMITE',
	 'prenom' : 'LYSIAN',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '14668628',
	 'nom' : 'AIT SI ALI',
	 'prenom' : 'MOHAMED',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '16853309',
	 'nom' : 'BEN SIDI YACOUB',
	 'prenom' : 'AHMED',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '12160983',
	 'nom' : 'BESSAIES',
	 'prenom' : 'MYRIAM',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '15224833',
	 'nom' : 'MOUHMID',
	 'prenom' : 'SAMI',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '14271792',
	 'nom' : 'TAQUOI',
	 'prenom' : 'ALEXANDRE',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '14780511',
	 'nom' : 'AUPIAIS ',
	 'prenom' : 'ALEXIS',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '14279737',
	 'nom' : 'HOSSEIN',
	 'prenom' : 'MELANIE',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '10083070',
	 'nom' : 'DELVAINCOURT ',
	 'prenom' : 'ARTHUR',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '18809751',
	 'nom' : 'KADERI',
	 'prenom' : 'ARNAUD',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '15329880',
	 'nom' : 'MALUSIMUANGA ',
	 'prenom' : 'BLEDE',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '17852753',
	 'nom' : 'RONCHIN ',
	 'prenom' : 'BENOIT',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '16649742',
	 'nom' : 'CIMETIERE ',
	 'prenom' : 'SIMON',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '12873972',
	 'nom' : 'VILLAIN ',
	 'prenom' : 'THOMAS',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '17380099',
	 'nom' : 'YANAGIHARA',
	 'prenom' : 'KEITARO',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '14625420',
	 'nom' : 'GERMAIN',
	 'prenom' : 'CAMILLE',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '17472045',
	 'nom' : 'CHADLI',
	 'prenom' : 'ANASS',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '19479465',
	 'nom' : 'DEHIMI',
	 'prenom' : 'MALIK',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '11627548',
	 'nom' : 'EL ATI',
	 'prenom' : 'FOUAD',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '19104844',
	 'nom' : 'GORSKI',
	 'prenom' : 'CHARLES',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '19741351',
	 'nom' : 'LORTHIOS',
	 'prenom' : 'VICTOR',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '18539405',
	 'nom' : 'NAJAFI',
	 'prenom' : 'SHIDEH',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '18733723',
	 'nom' : 'SOUMAILI',
	 'prenom' : 'AKRAM',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '10625306',
	 'nom' : 'ANNEBIQUE',
	 'prenom' : 'RENAUD',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '19785508',
	 'nom' : 'HERMOIRE ',
	 'prenom' : 'LOIC',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '15225678',
	 'nom' : 'ZOUHAIRI',
	 'prenom' : 'ANAS',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '13750875',
	 'nom' : 'BOUHSINA',
	 'prenom' : 'ILIAS',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '16253099',
	 'nom' : 'KOUDRI',
	 'prenom' : 'HIDIANE',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '19681184',
	 'nom' : 'OUARDI',
	 'prenom' : 'ANASS',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '11975754',
	 'nom' : 'GAUTHIER',
	 'prenom' : 'NOLAN',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '16445981',
	 'nom' : 'TEIXEIRA',
	 'prenom' : 'MORGANE',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '11674533',
	 'nom' : 'LEGRAIN',
	 'prenom' : 'BRYAN',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '19491231',
	 'nom' : 'CAVALIER',
	 'prenom' : 'FABIEN',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '14075536',
	 'nom' : 'JOULAINI',
	 'prenom' : 'SAMI',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '12655951',
	 'nom' : 'FEUTRIER',
	 'prenom' : 'SIMON',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '14401080',
	 'nom' : 'HALABI',
	 'prenom' : 'SAMI',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '14881015',
	 'nom' : 'PATINIER',
	 'prenom' : 'ANNE-CLAIRE',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '14679351',
	 'nom' : 'SOUBEIRAN',
	 'prenom' : 'MAUDE',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '16167103',
	 'nom' : 'HALABI EL',
	 'prenom' : 'SAMY',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '19116592',
	 'nom' : 'ORIGLIA',
	 'prenom' : 'TEDJANY',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '13879511',
	 'nom' : 'FOURNIER',
	 'prenom' : 'MAXENCE',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '13738540',
	 'nom' : 'GENTRIC',
	 'prenom' : 'GABRIELLE',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '17301563',
	 'nom' : 'ADJABI',
	 'prenom' : 'BILAL',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '12449724',
	 'nom' : 'DRIOUICH',
	 'prenom' : 'YASSINE',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '12220399',
	 'nom' : 'LOUIFI',
	 'prenom' : 'CHEYMA',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '14435770',
	 'nom' : 'CORREIA',
	 'prenom' : 'LAURE',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '12469354',
	 'nom' : 'GRANDJEAN',
	 'prenom' : 'SYLVAIN',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '13500455',
	 'nom' : 'EL HAJMI',
	 'prenom' : 'FATIMA',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '14876881',
	 'nom' : 'LAREDJ',
	 'prenom' : 'EL MEHDI',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '15969367',
	 'nom' : 'BEKKAJ',
	 'prenom' : 'FAICAL',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '13152518',
	 'nom' : 'GRANDJEAN',
	 'prenom' : 'SYLVAIN',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '15432260',
	 'nom' : 'BOUNAJEM',
	 'prenom' : 'GABRIEL',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '15539308',
	 'nom' : 'PETRYKOWSKI ',
	 'prenom' : 'CHLOE',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '14195997',
	 'nom' : 'HUDZIK',
	 'prenom' : 'CLARA',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '19585441',
	 'nom' : 'STEENKISTE',
	 'prenom' : 'JEREMY',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '14318030',
	 'nom' : 'MIAZEK',
	 'prenom' : 'ALEXANDRE',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '19595552',
	 'nom' : 'GUO',
	 'prenom' : 'KAIQI',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '13222885',
	 'nom' : 'HOUTEKIET',
	 'prenom' : 'THOMAS',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '14407161',
	 'nom' : 'KRZEMKOWSKI',
	 'prenom' : 'VINCENT',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '13984057',
	 'nom' : 'AIT EL AOUAD',
	 'prenom' : 'SALIMA',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '12012702',
	 'nom' : 'BOURELLE',
	 'prenom' : 'MARIE',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '16583129',
	 'nom' : 'BRUNEL',
	 'prenom' : 'VINCENT',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '14485903',
	 'nom' : 'GOSSELIN',
	 'prenom' : 'MARTIN',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '18902375',
	 'nom' : 'BELLAL',
	 'prenom' : 'ALEXANDRE',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '11641646',
	 'nom' : 'CAUDAL',
	 'prenom' : 'FALCHU',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '17439571',
	 'nom' : 'LEGUILLETTE',
	 'prenom' : 'CLEMENCE',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '11450852',
	 'nom' : 'DI SALVO',
	 'prenom' : 'ADRIANO',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '17444444',
	 'nom' : 'CZEKALLA',
	 'prenom' : 'THOMAS',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '19697184',
	 'nom' : 'DELVAL ',
	 'prenom' : 'THIBAULT',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '19404311',
	 'nom' : 'DUBAIL ',
	 'prenom' : 'DONIA',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '16389096',
	 'nom' : 'PONCELET ',
	 'prenom' : 'MATHIEU',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '11995521',
	 'nom' : 'REQUILLART-DOLE',
	 'prenom' : 'PAUL',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '16052067',
	 'nom' : 'ABDOUL-RAZACK HARED',
	 'prenom' : 'MOHAMED',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '12078972',
	 'nom' : 'FEDDAL ',
	 'prenom' : 'NORDINE',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '11583353',
	 'nom' : 'BENALLAL ',
	 'prenom' : 'REDOUANE',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '10243909',
	 'nom' : 'WENZEL ',
	 'prenom' : 'LUCILE',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '18523740',
	 'nom' : 'MAZZELLA ',
	 'prenom' : 'CORENTIN',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '10542688',
	 'nom' : 'MOTUELLE ',
	 'prenom' : 'QUENTIN',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '12834608',
	 'nom' : 'DEMAILLY',
	 'prenom' : 'THOMAS',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '15197586',
	 'nom' : 'COMBALBERT',
	 'prenom' : 'HUGO',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '16488981',
	 'nom' : 'LEMESLE ',
	 'prenom' : 'MARTIN',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '17342298',
	 'nom' : 'SEMAIL',
	 'prenom' : 'KEVIN',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '14986425',
	 'nom' : 'DELVALLE ',
	 'prenom' : 'NICOLAS',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '13660495',
	 'nom' : 'GUEBILI',
	 'prenom' : 'YOUCEF',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '19144344',
	 'nom' : 'NGOUOLALI KISSE',
	 'prenom' : 'KELLY',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '17043475',
	 'nom' : 'BARBILLON ',
	 'prenom' : 'ALEXANDRE',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '10442274',
	 'nom' : 'WATRELOS ',
	 'prenom' : 'JEREMY',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '16838695',
	 'nom' : 'BOUTILLIER',
	 'prenom' : 'CEDRIC',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '18993979',
	 'nom' : 'MARTEL',
	 'prenom' : 'VINCENT',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '11548367',
	 'nom' : 'CHEVALIER',
	 'prenom' : 'ARTHUR',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '19624839',
	 'nom' : 'WATRELOS',
	 'prenom' : 'AMANDINE',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '15900909',
	 'nom' : 'CIBOULLE--ROILLET',
	 'prenom' : 'JULIEN',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '18262643',
	 'nom' : 'DZIURLA',
	 'prenom' : 'DAVID',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '11678760',
	 'nom' : 'LASSELIN',
	 'prenom' : 'TEDDY',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '12837802',
	 'nom' : 'MACRELLE',
	 'prenom' : 'SIMON',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '18033818',
	 'nom' : 'DEMOULIN',
	 'prenom' : 'ADRIEN',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '14965040',
	 'nom' : 'ISRAEL',
	 'prenom' : 'RICHARD',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '14820395',
	 'nom' : 'MICHEL',
	 'prenom' : 'ORBRIA',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '16921694',
	 'nom' : 'DUBRULLE',
	 'prenom' : 'FABIAN',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '11680981',
	 'nom' : 'AUBEELUCK',
	 'prenom' : 'MERVIN',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '13962403',
	 'nom' : 'CAMERLYNCK',
	 'prenom' : 'ROMAIN',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '16885714',
	 'nom' : 'COMBALBERT',
	 'prenom' : 'HUGO',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '11478478',
	 'nom' : 'NOMSEMM',
	 'prenom' : 'BERNARD',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '16975339',
	 'nom' : 'VANHEMS',
	 'prenom' : 'FLORIAN',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '11828125',
	 'nom' : 'HOSSAM ODA',
	 'prenom' : 'Mohamed',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '19945482',
	 'nom' : 'LHOUMMANI ',
	 'prenom' : 'MOHAMMED OUSSAMA',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '10836037',
	 'nom' : 'DEGREMONT ',
	 'prenom' : 'CORALIE',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '19654027',
	 'nom' : 'DESTOMBE ',
	 'prenom' : 'CLEMENCE',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '16172507',
	 'nom' : 'HERREMAN ',
	 'prenom' : 'EVA',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '13937062',
	 'nom' : 'DESCAMPS ',
	 'prenom' : 'JULIEN',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '10169471',
	 'nom' : 'AIT AMEUR',
	 'prenom' : 'REIZLANE',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '13654238',
	 'nom' : 'CHAKIM',
	 'prenom' : 'HABIB',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '16079101',
	 'nom' : 'BACO MAHADALI',
	 'prenom' : 'WATTOINE',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '12738818',
	 'nom' : 'ATTOUMANI',
	 'prenom' : 'SYLVAIN',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '12986423',
	 'nom' : 'DE ALMEIDA',
	 'prenom' : 'RODRIGUE',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '19455086',
	 'nom' : 'HADRAMI ',
	 'prenom' : 'OUSSAMA OMAR',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '10893255',
	 'nom' : 'DESCAMPS',
	 'prenom' : 'GAUTHIER',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '10625515',
	 'nom' : 'VANDAMME',
	 'prenom' : 'CLAIRE',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '11811604',
	 'nom' : 'VANDOME',
	 'prenom' : 'CLEMENT',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '13720546',
	 'nom' : 'DESCAMPS',
	 'prenom' : 'KEVIN',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '15038445',
	 'nom' : 'FRYSON',
	 'prenom' : 'ROMANE',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '10689844',
	 'nom' : 'LASSON',
	 'prenom' : 'PIERRE',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '16986640',
	 'nom' : 'ADOUANE',
	 'prenom' : 'SHERAZADE',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '17921770',
	 'nom' : 'COSSON',
	 'prenom' : 'LAURENT',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '19268208',
	 'nom' : 'DEDEYNE',
	 'prenom' : 'QUENTIN',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '16860149',
	 'nom' : 'DEFFONTAINE',
	 'prenom' : 'MARTIN',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '10937457',
	 'nom' : 'EDHMINE',
	 'prenom' : 'MARIEM',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '11126588',
	 'nom' : 'MIMOUNI',
	 'prenom' : 'MOHAMMED AMINE',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '16160882',
	 'nom' : 'RAGHANI',
	 'prenom' : 'ATTIK',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '16311491',
	 'nom' : 'URUJENI',
	 'prenom' : 'GISELE',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '16232074',
	 'nom' : 'MEQUINION ',
	 'prenom' : 'MARIE',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '17313205',
	 'nom' : 'SOUMENAT',
	 'prenom' : 'ALDRYC',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '18081854',
	 'nom' : 'HOTTIN',
	 'prenom' : 'ANDREAS',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '17121114',
	 'nom' : 'KABBANI',
	 'prenom' : 'Mazen',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '16182887',
	 'nom' : 'BERMYN ',
	 'prenom' : 'YVES-MARIE',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '19932556',
	 'nom' : 'MATHON ',
	 'prenom' : 'ANTHONY',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '12279161',
	 'nom' : 'PANIEN',
	 'prenom' : 'ALEXIS',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '11755261',
	 'nom' : 'CAPUANO ',
	 'prenom' : 'JEAN-LOUIS',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '11782031',
	 'nom' : 'FAUVIN ',
	 'prenom' : 'NJAKA',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '14057635',
	 'nom' : 'MARTINS BAIA',
	 'prenom' : 'JOANA FILIPA',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '13049532',
	 'nom' : 'AVELINE ',
	 'prenom' : 'FANNY',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '18415992',
	 'nom' : 'CHAVANEL ',
	 'prenom' : 'JUSTINE',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '18858250',
	 'nom' : 'FORTIN ',
	 'prenom' : 'CELIA',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '19271482',
	 'nom' : 'SEYYANI-LAKRIZI',
	 'prenom' : 'NIZAR',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '12513374',
	 'nom' : 'BETRANCOURT',
	 'prenom' : 'REMY',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '11167514',
	 'nom' : 'BOULANT ',
	 'prenom' : 'JOFFREY',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '15443833',
	 'nom' : 'OUIKENE',
	 'prenom' : 'KOCEILA',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '16666609',
	 'nom' : 'RANSON ',
	 'prenom' : 'CINDY',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '11935740',
	 'nom' : 'FLAMANT ',
	 'prenom' : 'ANTOINE',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '19033780',
	 'nom' : 'ENGRAND',
	 'prenom' : 'LIONEL',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '13129737',
	 'nom' : 'KUNSANGABO NDONGALA',
	 'prenom' : 'BERFY',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '16823707',
	 'nom' : 'QUERIN ',
	 'prenom' : 'DAVID',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '19189451',
	 'nom' : 'LEGRAND ',
	 'prenom' : 'DAMIEN',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '16844776',
	 'nom' : 'CREPIN',
	 'prenom' : 'MATHIEU',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '12111116',
	 'nom' : 'DENDONCKER ',
	 'prenom' : 'FLORIAN',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '13293266',
	 'nom' : 'MASSON',
	 'prenom' : 'FLORENT',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '11099811',
	 'nom' : 'ESSIANE',
	 'prenom' : 'ABEL-EDOUARD',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '18097368',
	 'nom' : 'VERKINDERE',
	 'prenom' : 'JULIEN',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '18589690',
	 'nom' : 'DEHAINE',
	 'prenom' : 'ZOE',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '17278640',
	 'nom' : 'FLAMENT',
	 'prenom' : 'LUC',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '14524768',
	 'nom' : 'MARTIN',
	 'prenom' : 'AURELIE',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '12223820',
	 'nom' : 'RAHMANI AZAD',
	 'prenom' : 'EDOUARD',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '12384421',
	 'nom' : 'SZAFONI',
	 'prenom' : 'LOIC',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '19816143',
	 'nom' : 'CORDONNIER',
	 'prenom' : 'CORENTIN',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '10685937',
	 'nom' : 'GILMANT',
	 'prenom' : 'LUCAS',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '17317628',
	 'nom' : 'MULLANU',
	 'prenom' : 'RAPHAEL',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '14341328',
	 'nom' : 'FELLENBERG',
	 'prenom' : 'SEBASTIEN',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '12042413',
	 'nom' : 'HASSAN',
	 'prenom' : 'CHARIF',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '14984136',
	 'nom' : 'MARTIN',
	 'prenom' : 'GAETAN',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '14489915',
	 'nom' : 'OUAZIN',
	 'prenom' : 'ABDERRAHIM',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '19146788',
	 'nom' : 'STEVENOT',
	 'prenom' : 'EMERIC',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '13743956',
	 'nom' : 'OUCHAN',
	 'prenom' : 'JAMAL',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '15534794',
	 'nom' : 'TRAISNEL',
	 'prenom' : 'GAUTHIER',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '10618993',
	 'nom' : 'TASSIN',
	 'prenom' : 'GAUTHIER',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '19701030',
	 'nom' : 'VANDENEECKHOUTTE',
	 'prenom' : 'AZILLIS',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '18923871',
	 'nom' : 'BOUCHNAYAF',
	 'prenom' : 'OMAR',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '18041802',
	 'nom' : 'BRYDENBACH',
	 'prenom' : 'LUDOVIC',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '13835469',
	 'nom' : 'DUQUENNE',
	 'prenom' : 'ROBIN',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '16272153',
	 'nom' : 'GUIBINGA',
	 'prenom' : 'CHARES KASSANDRA',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '17248877',
	 'nom' : 'MARTIN',
	 'prenom' : 'RONAN',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '17716181',
	 'nom' : 'BAUVIN',
	 'prenom' : 'MANON',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '15672130',
	 'nom' : 'CAPANNELLI',
	 'prenom' : 'JEROME',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '15023598',
	 'nom' : 'LEQUIN',
	 'prenom' : 'PIERRE',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '16203106',
	 'nom' : 'MARTIN',
	 'prenom' : 'LOUIS',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '16090833',
	 'nom' : 'MASTIN',
	 'prenom' : 'CLEMENT',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '12101793',
	 'nom' : 'CAYRON',
	 'prenom' : 'VALENTIN',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '10009491',
	 'nom' : 'GELOEN',
	 'prenom' : 'CLEMENT',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '13543734',
	 'nom' : 'MEHANNA',
	 'prenom' : 'NAIF',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '14374017',
	 'nom' : 'POTVIN',
	 'prenom' : 'LEA',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '12283798',
	 'nom' : 'BEGHIN',
	 'prenom' : 'LUCAS',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '11903119',
	 'nom' : 'DUQUENOY',
	 'prenom' : 'ANTOINE',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '14182508',
	 'nom' : 'GOEMAN-SION',
	 'prenom' : 'CLEMENCE',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '16301158',
	 'nom' : 'DEBAENE',
	 'prenom' : 'GAEL',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '13307929',
	 'nom' : 'LEGRAND',
	 'prenom' : 'PIERRE YVES',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '12332724',
	 'nom' : 'TADJINE',
	 'prenom' : 'MOHAMED',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '16426903',
	 'nom' : 'LAACHOURI',
	 'prenom' : 'KARIM',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '11278258',
	 'nom' : 'PEPDJONOVIC',
	 'prenom' : 'MARIANA',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '15772645',
	 'nom' : 'QUESNOT',
	 'prenom' : 'MARIE',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '11627908',
	 'nom' : 'RAFANOMEZANTSOA',
	 'prenom' : 'ROVA',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '16394289',
	 'nom' : 'RATINON',
	 'prenom' : 'JEAN-FRANCOIS',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '11621395',
	 'nom' : 'CAUDRON ',
	 'prenom' : 'MYLENE',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '17191267',
	 'nom' : 'GUERROUI ',
	 'prenom' : 'ADAM',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '13788183',
	 'nom' : 'DELAFOSSE',
	 'prenom' : 'VICTOR',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '13309643',
	 'nom' : 'DARKAOUI',
	 'prenom' : 'OTHMANE',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '18768265',
	 'nom' : 'PLANCOT',
	 'prenom' : 'ERWANN',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '16078600',
	 'nom' : 'DELAPORTE',
	 'prenom' : 'MORGAN',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '10644525',
	 'nom' : 'GUILLON ',
	 'prenom' : 'DAVID',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '12455105',
	 'nom' : 'DIALLO',
	 'prenom' : 'ALSENY',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '13339352',
	 'nom' : 'GILLOOTS ',
	 'prenom' : 'FELIX',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '12299201',
	 'nom' : 'HAMRAOUI ',
	 'prenom' : 'WIDADE',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '10633729',
	 'nom' : 'CHENIOUNI',
	 'prenom' : 'RABIR',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '14733841',
	 'nom' : 'OUARKOUB ',
	 'prenom' : 'FERIEL',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '19519468',
	 'nom' : 'RAVELOMANANTSOA',
	 'prenom' : 'DINA',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '15718785',
	 'nom' : 'SANSAOUI ',
	 'prenom' : 'YASSINE',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '17904996',
	 'nom' : 'PANICO ',
	 'prenom' : 'KEVIN',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '14571265',
	 'nom' : 'DENICOURT',
	 'prenom' : 'LOUIS',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '18772271',
	 'nom' : 'DIALLO',
	 'prenom' : 'MACKY',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '14297508',
	 'nom' : 'FOURMOND',
	 'prenom' : 'DAVID',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '10561337',
	 'nom' : 'BOUSSOUGHA',
	 'prenom' : 'AMIR',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '16981857',
	 'nom' : 'ALI SOUBANEH',
	 'prenom' : 'KADIDJA',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '14452009',
	 'nom' : 'GITERO ',
	 'prenom' : 'ROBERT CHRISTIAN',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '13553987',
	 'nom' : 'KEMAJOU',
	 'prenom' : 'KEVIN',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '19374365',
	 'nom' : 'LESCROART',
	 'prenom' : 'GUILLAUME',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '16530529',
	 'nom' : 'LAMBLOT',
	 'prenom' : 'JONATHAN',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '12739037',
	 'nom' : 'DIALLO',
	 'prenom' : 'OUMOU KOULTOUMY',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '12209945',
	 'nom' : 'FRANCOIS',
	 'prenom' : 'NELSON',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '13029606',
	 'nom' : 'RATINON',
	 'prenom' : 'JEAN-FRANCOIS',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '11391220',
	 'nom' : 'KITOKO LANDY',
	 'prenom' : 'LANDRY',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '14451489',
	 'nom' : 'PARASOTE',
	 'prenom' : 'CELINE',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '16696684',
	 'nom' : 'POUABOU',
	 'prenom' : 'CATHIE',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '19582846',
	 'nom' : 'KHALDOUNE',
	 'prenom' : 'ANASS',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '15960037',
	 'nom' : 'LANGLOIS',
	 'prenom' : 'MATHIS',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '12503952',
	 'nom' : 'RASOLONDRAINIBE',
	 'prenom' : 'NIRINA',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '17024448',
	 'nom' : 'BALITOUT',
	 'prenom' : 'XAVIER',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '13001140',
	 'nom' : 'BELKHODJA',
	 'prenom' : 'AMINE',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '17744231',
	 'nom' : 'HAMDAOUI',
	 'prenom' : 'MOHAMED',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '13222847',
	 'nom' : 'LESCROART',
	 'prenom' : 'AUDREY',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '19479636',
	 'nom' : 'DELAPORTE',
	 'prenom' : 'MAEVA',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '12421855',
	 'nom' : 'GRANIOU',
	 'prenom' : 'JULIETTE',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '11264991',
	 'nom' : 'FRANCOIS',
	 'prenom' : 'THOMAS',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '19659729',
	 'nom' : 'ALCODORI',
	 'prenom' : 'FRANCOIS',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '15102973',
	 'nom' : 'HAMLAOUI CHAREUF',
	 'prenom' : 'KEZIAH',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '14672399',
	 'nom' : 'RAKOTOMANDIMBY',
	 'prenom' : 'TSIRINIAINA',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '17673286',
	 'nom' : 'BEN ROMDHANE',
	 'prenom' : 'YOUSSEF',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '17438939',
	 'nom' : 'DEREPPE',
	 'prenom' : 'JULIETTE',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '15073202',
	 'nom' : 'PHILIPPE ',
	 'prenom' : 'JEAN-BAPTISTE',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '16666386',
	 'nom' : 'PHILIPPOT ',
	 'prenom' : 'GREGOIRE',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '15019349',
	 'nom' : 'SZCZEPANSKI',
	 'prenom' : 'DARIA',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '12467715',
	 'nom' : 'SPROCQ ',
	 'prenom' : 'SIMON',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '18980001',
	 'nom' : 'PLANCQ',
	 'prenom' : 'BRUNO',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '19433054',
	 'nom' : 'DELMER',
	 'prenom' : 'CLEMENT',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '10975944',
	 'nom' : 'LECLERE',
	 'prenom' : 'ALBAN',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '18632079',
	 'nom' : 'DUSSART',
	 'prenom' : 'JORDAN',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '10792892',
	 'nom' : 'TEXIER',
	 'prenom' : 'LEANE',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '16758039',
	 'nom' : 'HAIDAR AHMAD',
	 'prenom' : 'OUNSY',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '10450095',
	 'nom' : 'LE MERO',
	 'prenom' : 'PAULINE',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '12581542',
	 'nom' : 'MELLARD ',
	 'prenom' : 'ALLAN',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '15687841',
	 'nom' : 'DEQUIRET ',
	 'prenom' : 'MICKAEL',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '10118559',
	 'nom' : 'LECLERCQ ',
	 'prenom' : 'KARIM',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '18115305',
	 'nom' : 'SALGUR ',
	 'prenom' : 'IBRAHIM',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '10649967',
	 'nom' : 'GOMBERT ',
	 'prenom' : 'MELINE',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '14463818',
	 'nom' : 'TEXIER',
	 'prenom' : 'LEANE',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '13274093',
	 'nom' : 'COSSART ',
	 'prenom' : 'MARION',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '14284339',
	 'nom' : 'HALIPRE',
	 'prenom' : 'KEVIN',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '11751358',
	 'nom' : 'CHATER',
	 'prenom' : 'HAMZA',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '11793616',
	 'nom' : 'DELMER',
	 'prenom' : 'CLEMENT',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '17890760',
	 'nom' : 'LECLERC ',
	 'prenom' : 'EMILIE',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '18448065',
	 'nom' : 'MILCARECK ',
	 'prenom' : 'GWENAEL',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '18914073',
	 'nom' : 'AUDIER',
	 'prenom' : 'FLORIAN',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '14982938',
	 'nom' : 'OUTTERYCK ',
	 'prenom' : 'MAXIME',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '16306916',
	 'nom' : 'VAMOUR',
	 'prenom' : 'VALENTIN',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '13966456',
	 'nom' : 'LECLERCQ',
	 'prenom' : 'QUENTIN',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '16869365',
	 'nom' : 'POUPART ',
	 'prenom' : 'VALENTIN',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '15868594',
	 'nom' : 'DAUMERIE',
	 'prenom' : 'FLORIAN',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '12737207',
	 'nom' : 'DELECROIX ',
	 'prenom' : 'GAETAN',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '12386952',
	 'nom' : 'MUSTAR ',
	 'prenom' : 'LOIC',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '17173433',
	 'nom' : 'VANTORRE ',
	 'prenom' : 'FABIEN',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '14824514',
	 'nom' : 'BONNARD',
	 'prenom' : 'RENAUD',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '12017530',
	 'nom' : 'HEMBERT',
	 'prenom' : 'MARTIN',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '15241291',
	 'nom' : 'SHCHERBAKOVA',
	 'prenom' : 'IULIIA',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '19333359',
	 'nom' : 'CHOUIREF',
	 'prenom' : 'YLYES',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '18500184',
	 'nom' : 'DELFORGE',
	 'prenom' : 'SAVIGNAIN',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '13584413',
	 'nom' : 'SCHEIRLINCK',
	 'prenom' : 'CLEMENT',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '16030653',
	 'nom' : 'AGAYER',
	 'prenom' : 'MERYEM',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '14600843',
	 'nom' : 'LACOURTE',
	 'prenom' : 'JONATHAN',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '16241574',
	 'nom' : 'TARTAR',
	 'prenom' : 'ALBAN',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '14964630',
	 'nom' : 'LECLERCQ',
	 'prenom' : 'ELIAS',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '15681032',
	 'nom' : 'LECLERCQ',
	 'prenom' : 'FLORIAN',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '11155757',
	 'nom' : 'LEFEBRE',
	 'prenom' : 'AXEL',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '18226003',
	 'nom' : 'RAVIART',
	 'prenom' : 'AURELIEN',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '12476664',
	 'nom' : 'SOLDERA',
	 'prenom' : 'QUENTIN',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '14054956',
	 'nom' : 'ESQUERRE-POURTERE',
	 'prenom' : 'ARTHUR',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '17108041',
	 'nom' : 'HAIDARA',
	 'prenom' : 'STEEVE',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '11777169',
	 'nom' : 'LENOIR',
	 'prenom' : 'JEREMY',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '18238843',
	 'nom' : 'ZOUHIR',
	 'prenom' : 'ADNANE',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '19331408',
	 'nom' : 'DANVERT',
	 'prenom' : 'HUGO',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '12752771',
	 'nom' : 'LASSERON',
	 'prenom' : 'ANTOINE',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '12369594',
	 'nom' : 'GOSSART',
	 'prenom' : 'CLEMENT',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '19863122',
	 'nom' : 'LETOURNEUR',
	 'prenom' : 'LOUIS',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '17314495',
	 'nom' : 'LEFEVRE',
	 'prenom' : 'CLEMENT',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '15859896',
	 'nom' : 'LEMAIRE',
	 'prenom' : 'STEVEN',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '14781720',
	 'nom' : 'MANGARD',
	 'prenom' : 'LEO',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '14175001',
	 'nom' : 'HOCHART',
	 'prenom' : 'QUENTIN',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '14837919',
	 'nom' : 'MARRER',
	 'prenom' : 'VALENTIN MAURICE',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '14578437',
	 'nom' : 'RIBEIRO',
	 'prenom' : 'PAUL',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '18055542',
	 'nom' : 'RICHARD',
	 'prenom' : 'ANDY',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '15869119',
	 'nom' : 'CHIGURI',
	 'prenom' : 'ILIAS ',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '15233006',
	 'nom' : 'KIMOUR',
	 'prenom' : 'INES',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '14409189',
	 'nom' : 'DEROOSE',
	 'prenom' : 'LEONARD',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '16513909',
	 'nom' : 'DUBOIS',
	 'prenom' : 'OPHELIE',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '14267564',
	 'nom' : 'SOUAISSA',
	 'prenom' : 'AMZA',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '14164449',
	 'nom' : 'ASSASS ',
	 'prenom' : 'YOUNESS',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '11493621',
	 'nom' : 'HARGAS',
	 'prenom' : 'TASSADIT',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '15999219',
	 'nom' : 'NGUESSAN',
	 'prenom' : 'MODJUE NOEMIE',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '15181987',
	 'nom' : 'BELHOSTE',
	 'prenom' : 'Antoine',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '12219735',
	 'nom' : 'DUBOISDENDIEN ',
	 'prenom' : 'VIVIEN',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '10593887',
	 'nom' : 'PARSIS',
	 'prenom' : 'THIBAULT',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '17814314',
	 'nom' : 'DUPUIS ',
	 'prenom' : 'ALEXIS',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '19654233',
	 'nom' : 'DUPUIS ',
	 'prenom' : 'FLORENTIN',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '12483567',
	 'nom' : 'CAMPISTRON ',
	 'prenom' : 'THOMAS',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '16653052',
	 'nom' : 'DESBISSCHOP',
	 'prenom' : 'DAVID',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '11579795',
	 'nom' : 'PRUVOST ',
	 'prenom' : 'JOHAN',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '10861020',
	 'nom' : 'SENOUSSI ASSIM',
	 'prenom' : 'TAREK',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '12488848',
	 'nom' : 'DUBUISSON ',
	 'prenom' : 'FABIEN',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '15085115',
	 'nom' : 'ANDRISSEN',
	 'prenom' : 'ROBIN',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '13324823',
	 'nom' : 'CALINSKI',
	 'prenom' : 'JULIEN',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '12470550',
	 'nom' : 'DUPUIS',
	 'prenom' : 'JULIEN',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '18449226',
	 'nom' : 'CONGOS',
	 'prenom' : 'ROMAIN',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '15506768',
	 'nom' : 'EL ASSRAOUI',
	 'prenom' : 'HAMZA',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '10410996',
	 'nom' : 'LECLUSE',
	 'prenom' : 'ALEXIS',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '13811361',
	 'nom' : 'LEPERS',
	 'prenom' : 'MATTHIEU',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '12654667',
	 'nom' : 'DIA',
	 'prenom' : 'SEKOU',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '17346063',
	 'nom' : 'FARISSI',
	 'prenom' : 'MOHAMED',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '13355310',
	 'nom' : 'LOUNAS',
	 'prenom' : 'SARRA',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '16352138',
	 'nom' : 'MATHIS',
	 'prenom' : 'CLEMENT',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '16685906',
	 'nom' : 'TAOUSSI',
	 'prenom' : 'AMINE              21ects/10,8',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '19801666',
	 'nom' : 'BRIOIS',
	 'prenom' : 'ZOE',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '14380638',
	 'nom' : 'DUFOSSE',
	 'prenom' : 'GREGOIRE',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '14081695',
	 'nom' : 'BEAUSSART',
	 'prenom' : 'JEAN-LOUP',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '13842348',
	 'nom' : 'MERCUSOT',
	 'prenom' : 'GREGOIRE',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '11681920',
	 'nom' : 'DUFRESNE',
	 'prenom' : 'ERWAN',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '13262459',
	 'nom' : 'PRUVOST',
	 'prenom' : 'OCEANE',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '11870716',
	 'nom' : 'JOCLAS',
	 'prenom' : 'THOMAS',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '17797979',
	 'nom' : 'MARMUS',
	 'prenom' : 'AUGUSTIN',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '11377416',
	 'nom' : 'BEDISSE',
	 'prenom' : 'RAFIK',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '12035458',
	 'nom' : 'BELLIT',
	 'prenom' : 'NACIM',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '19313187',
	 'nom' : 'CONRATTE',
	 'prenom' : 'PIERRE',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '14114711',
	 'nom' : 'ESSANTOUHI',
	 'prenom' : 'ABDELJALIL',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '19036308',
	 'nom' : 'SEBERT ',
	 'prenom' : 'CAMILLE',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '15481959',
	 'nom' : 'GOUBET',
	 'prenom' : 'GHISLAIN',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '10374832',
	 'nom' : 'MONNET',
	 'prenom' : 'ALEXIS',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '14553164',
	 'nom' : 'DUSAUTOIR ',
	 'prenom' : 'THEO',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '12101960',
	 'nom' : 'FAUDOT-MIGUET',
	 'prenom' : 'SAMUEL',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '13479574',
	 'nom' : 'DUPONT ',
	 'prenom' : 'VICTOR',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '14009361',
	 'nom' : 'MEGUETTA',
	 'prenom' : 'FAROUK',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '17359553',
	 'nom' : 'EL ATTAR ',
	 'prenom' : 'YASSIR',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '17175525',
	 'nom' : 'HENNETON ',
	 'prenom' : 'LAURY',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '18113396',
	 'nom' : 'EDMONT ',
	 'prenom' : 'LUCIEN',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '19980644',
	 'nom' : 'BARBET',
	 'prenom' : 'BENJAMIN',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '15567670',
	 'nom' : 'CARRETTE ',
	 'prenom' : 'BLANDINE',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '18844344',
	 'nom' : 'DEFAUT ',
	 'prenom' : 'MAXENCE',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '13542837',
	 'nom' : 'PARENT',
	 'prenom' : 'CAMILLE',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '11642806',
	 'nom' : 'REDANT ',
	 'prenom' : 'BENJAMIN',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '15242217',
	 'nom' : 'BUNIET',
	 'prenom' : 'EMILIE',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '12961579',
	 'nom' : 'CABLAT',
	 'prenom' : 'JEAN BAPTISTE',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '14938158',
	 'nom' : 'FAUDOT-MIGUET',
	 'prenom' : 'SAMUEL',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '10696297',
	 'nom' : 'ZANETTI',
	 'prenom' : 'NICOLAS',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '18837564',
	 'nom' : 'DECOSTER ',
	 'prenom' : 'TIMOTHEE',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '13501757',
	 'nom' : 'LAMOOT',
	 'prenom' : 'ROMAIN',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '15020684',
	 'nom' : 'RUIVET ',
	 'prenom' : 'TITOUAN',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '17301411',
	 'nom' : 'CORRETEL',
	 'prenom' : 'FABIEN',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '13024033',
	 'nom' : 'LEMAITRE',
	 'prenom' : 'Antoine',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '17499940',
	 'nom' : 'BUCHET',
	 'prenom' : 'VICTOR',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '11674699',
	 'nom' : 'HARRAT',
	 'prenom' : 'NAIM',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '19928971',
	 'nom' : 'TANOUTI',
	 'prenom' : 'YASSINE',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '18312367',
	 'nom' : 'BAH',
	 'prenom' : 'THIERNO AMADOU',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '14384577',
	 'nom' : 'BEDART',
	 'prenom' : 'CLELIA',
	 'formation' : 'SESI',
	 'groupe' : '53'
	},

	{'nip' : '11152409',
	 'nom' : 'AISSAT',
	 'prenom' : 'ALI',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '15689317',
	 'nom' : 'EL ATTAR',
	 'prenom' : 'FATIMA ZOHRA',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '18400017',
	 'nom' : 'VARLET',
	 'prenom' : 'FAUSTINE',
	 'formation' : 'PEIP',
	 'groupe' : '14'
	},

	{'nip' : '13508128',
	 'nom' : 'ARDIET',
	 'prenom' : 'BENOIT',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '19572006',
	 'nom' : 'HAMMOUTI',
	 'prenom' : 'HAMIDA',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '19141453',
	 'nom' : 'SAHNOUNI',
	 'prenom' : 'OUMANI',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '15891980',
	 'nom' : 'THIBAULT',
	 'prenom' : 'SARAH',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '15565413',
	 'nom' : 'CHOMPUM',
	 'prenom' : 'APHISIT',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '19354215',
	 'nom' : 'CLABAUX ',
	 'prenom' : 'ANTOINE',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '18967965',
	 'nom' : 'COUROUBLE',
	 'prenom' : 'TANGUY',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '13921373',
	 'nom' : 'MEREAU',
	 'prenom' : 'SIMON',
	 'formation' : 'SESI',
	 'groupe' : '12'
	},

	{'nip' : '17935608',
	 'nom' : 'COSSOU ',
	 'prenom' : 'MANON',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '12174581',
	 'nom' : 'DURECU',
	 'prenom' : 'KARINE',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '18136617',
	 'nom' : 'LE COUTOUR',
	 'prenom' : 'QUENTIN',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '14046306',
	 'nom' : 'VANTOURS ',
	 'prenom' : 'FRANCOIS',
	 'formation' : 'SESI',
	 'groupe' : '13'
	},

	{'nip' : '19680344',
	 'nom' : 'BOUNOUAR ',
	 'prenom' : 'MOUNIR',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '16537240',
	 'nom' : 'ZERROUKI',
	 'prenom' : 'MOHAMED',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '14565701',
	 'nom' : 'EL KOUHEN',
	 'prenom' : 'Tarik',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '14125690',
	 'nom' : 'TREHOU',
	 'prenom' : 'LAURENE',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '14195292',
	 'nom' : 'YACHOU',
	 'prenom' : 'MOHAMMED',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '18055349',
	 'nom' : 'HEDDOU OUSSELLAM ',
	 'prenom' : 'FATIMA',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '14489766',
	 'nom' : 'HEDDOU OUSSELLAM ',
	 'prenom' : 'MOUNIR',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '13844273',
	 'nom' : 'PUCHAUX ',
	 'prenom' : 'LOIC',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '13955986',
	 'nom' : 'AL BOURKI ',
	 'prenom' : 'OSSAMA',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '12213354',
	 'nom' : 'AMRAOUI',
	 'prenom' : 'RAIS',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '10533418',
	 'nom' : 'DESREUMAUX ',
	 'prenom' : 'REMY',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '19770515',
	 'nom' : 'HAMDOUD',
	 'prenom' : 'RAYANE',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '11307965',
	 'nom' : 'VASSEUR ',
	 'prenom' : 'TEO',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '16182972',
	 'nom' : 'BENYOUSSEF',
	 'prenom' : 'ABDELHAKIM',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '16545504',
	 'nom' : 'MUBERUKA',
	 'prenom' : 'ALAIN',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '15367508',
	 'nom' : 'PULULU MPESI',
	 'prenom' : 'TATIANA',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '15892204',
	 'nom' : 'ROMBAUT ',
	 'prenom' : 'ANTOINE',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '18510470',
	 'nom' : 'WACHEUX ',
	 'prenom' : 'AYMERIC',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '14804380',
	 'nom' : 'WU',
	 'prenom' : 'YUEYAO',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '13465450',
	 'nom' : 'JUCHAULT DES JAMONIERES',
	 'prenom' : 'HENRI',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '12918566',
	 'nom' : 'KALAOUN',
	 'prenom' : 'OMAR',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '17049172',
	 'nom' : 'LEVEQUE',
	 'prenom' : 'AZZEDINE',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '11060822',
	 'nom' : 'MAHIEUX',
	 'prenom' : 'BAPTISTE',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '14665496',
	 'nom' : 'BADAOUI',
	 'prenom' : 'NACIM',
	 'formation' : 'SESI',
	 'groupe' : '43'
	},

	{'nip' : '19588521',
	 'nom' : 'HALMOUCHE',
	 'prenom' : 'MOURAD',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '13099496',
	 'nom' : 'CHAHOUAT',
	 'prenom' : 'TAOUFIK',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '17733914',
	 'nom' : 'HARROUD',
	 'prenom' : 'GUILLAUME',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '17792530',
	 'nom' : 'WITTOUCK',
	 'prenom' : 'JORDAN',
	 'formation' : 'SESI',
	 'groupe' : '51'
	},

	{'nip' : '18646709',
	 'nom' : 'BEKKOUCHE ',
	 'prenom' : 'MOHAMED',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '17266965',
	 'nom' : 'MAINGUET',
	 'prenom' : 'THEO',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '18229761',
	 'nom' : 'YACHOU',
	 'prenom' : 'LOUBNA',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '19388586',
	 'nom' : 'DESSOUDE',
	 'prenom' : 'ANTOINE',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '10887408',
	 'nom' : 'TILIOUINE ',
	 'prenom' : 'KEVIN YOUNES',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '13088399',
	 'nom' : 'HAUGOU',
	 'prenom' : 'CLEMENT',
	 'formation' : 'PEIP',
	 'groupe' : '11'
	},

	{'nip' : '18354981',
	 'nom' : 'MANSOURI',
	 'prenom' : 'ALEXI',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '17761657',
	 'nom' : 'DESOEUVRE',
	 'prenom' : 'FANNY',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '18422628',
	 'nom' : 'MOREAU',
	 'prenom' : 'NICOLASARTHUR',
	 'formation' : 'PEIP',
	 'groupe' : '15'
	},

	{'nip' : '11073363',
	 'nom' : 'KARTOUT',
	 'prenom' : 'ANIS',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '14058619',
	 'nom' : 'MAHFOUDH',
	 'prenom' : 'SAMY',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '11943643',
	 'nom' : 'VAN OVERTVELT',
	 'prenom' : 'YOANN',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '18476771',
	 'nom' : 'BONNEVAL ',
	 'prenom' : 'MELISANDE',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '13180188',
	 'nom' : 'DERREVEAUX ',
	 'prenom' : 'ANTHONY',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '14477132',
	 'nom' : 'VENDEVILLE ',
	 'prenom' : 'ADRIEN',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '12655971',
	 'nom' : 'VANHOVE ',
	 'prenom' : 'JULIEN',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '17134758',
	 'nom' : 'LEFEBVRE',
	 'prenom' : 'RYAN',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '17401286',
	 'nom' : 'LEFEBVRE',
	 'prenom' : 'ROBIN',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '18413929',
	 'nom' : 'DESREVEAUX',
	 'prenom' : 'NATHAN',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '15109863',
	 'nom' : 'BOGDEV',
	 'prenom' : 'JIVKO',
	 'formation' : 'LICAM',
	 'groupe' : '1'
	},

	{'nip' : '13395673',
	 'nom' : 'DRUTOWSKI ',
	 'prenom' : 'VALENTIN',
	 'formation' : 'SESI',
	 'groupe' : '22'
	},

	{'nip' : '10131929',
	 'nom' : 'DIBAKWE',
	 'prenom' : 'FABIOLA',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '19213117',
	 'nom' : 'NEZERWE',
	 'prenom' : 'NINA SAMANTHA',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '12602035',
	 'nom' : 'LULKOWSKA',
	 'prenom' : 'KLAUDIA',
	 'formation' : 'SESI',
	 'groupe' : '41'
	},

	{'nip' : '18126461',
	 'nom' : 'ABDE WEDOUD',
	 'prenom' : 'MOHAMED',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '15582560',
	 'nom' : 'GUEREW',
	 'prenom' : 'THIERNO',
	 'formation' : 'SESI',
	 'groupe' : '54'
	},

	{'nip' : '15028205',
	 'nom' : 'LIU',
	 'prenom' : 'XIAOYU',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '17400487',
	 'nom' : 'SAVANXAYADETH',
	 'prenom' : 'VANNY-BRAYAN',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '11269662',
	 'nom' : 'SAVANXAYADETH ',
	 'prenom' : 'MARVIN',
	 'formation' : 'SESI',
	 'groupe' : '32'
	},

	{'nip' : '15630851',
	 'nom' : 'HAO',
	 'prenom' : 'XUECHAO',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '18768280',
	 'nom' : 'HULEUX',
	 'prenom' : 'ADRIEN',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '13133649',
	 'nom' : 'DUREUX',
	 'prenom' : 'LOUIS',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '14284440',
	 'nom' : 'RIBAUX',
	 'prenom' : 'EMMA',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '18822035',
	 'nom' : 'GAUDRY',
	 'prenom' : 'CHRISTOPHER',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '14743143',
	 'nom' : 'MOULAY ZEINE',
	 'prenom' : 'MOULAY ZEINE',
	 'formation' : 'SESI',
	 'groupe' : '14'
	},

	{'nip' : '12425026',
	 'nom' : 'AUVRAY ',
	 'prenom' : 'CLAIRE',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '11396479',
	 'nom' : 'DEBRAY ',
	 'prenom' : 'JULIE',
	 'formation' : 'SESI',
	 'groupe' : '21'
	},

	{'nip' : '16011948',
	 'nom' : 'ZBOZHYNSKA',
	 'prenom' : 'LARYNA',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '10601753',
	 'nom' : 'HARIDY',
	 'prenom' : 'OMAR',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '19688877',
	 'nom' : 'GORCZYCA',
	 'prenom' : 'PRISCILLIA',
	 'formation' : 'SESI',
	 'groupe' : '42'
	},

	{'nip' : '16911418',
	 'nom' : 'ARBLAY',
	 'prenom' : 'THOMAS',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '15069193',
	 'nom' : 'PTASZYNSKI',
	 'prenom' : 'VINCENT',
	 'formation' : 'SESI',
	 'groupe' : '52'
	},

	{'nip' : '10970173',
	 'nom' : 'FLEURY',
	 'prenom' : 'AMBROISE',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '17683372',
	 'nom' : 'POURRY',
	 'prenom' : 'FLORIAN',
	 'formation' : 'PEIP',
	 'groupe' : '12'
	},

	{'nip' : '16493104',
	 'nom' : 'MARKEY',
	 'prenom' : 'LAURE',
	 'formation' : 'PEIP',
	 'groupe' : '13'
	},

	{'nip' : '12816462',
	 'nom' : 'TEMPEZ',
	 'prenom' : 'CORENTIN',
	 'formation' : 'MASS',
	 'groupe' : '1'
	},

	{'nip' : '10818882',
	 'nom' : 'COUPEZ',
	 'prenom' : 'ELIE',
	 'formation' : 'MASS',
	 'groupe' : '2'
	},

	{'nip' : '12957376',
	 'nom' : 'SCHULZ',
	 'prenom' : 'MATHIEU',
	 'formation' : 'SESI',
	 'groupe' : '11'
	},

	{'nip' : '15236320',
	 'nom' : 'BODDEZ',
	 'prenom' : 'KENNY',
	 'formation' : 'SESI',
	 'groupe' : '23'
	},

	{'nip' : '14506060',
	 'nom' : 'BULTEZ ',
	 'prenom' : 'LAURIE',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '19574883',
	 'nom' : 'SAMIEZ ',
	 'prenom' : 'ANTOINE',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '10860793',
	 'nom' : 'THOREZ ',
	 'prenom' : 'JOSEPHINE',
	 'formation' : 'SESI',
	 'groupe' : '24'
	},

	{'nip' : '14878885',
	 'nom' : 'EL AZZOUZI',
	 'prenom' : 'HAMZA',
	 'formation' : 'SESI',
	 'groupe' : '31'
	},

	{'nip' : '18528939',
	 'nom' : 'RICHEZ',
	 'prenom' : 'FLORIAN',
	 'formation' : 'SESI',
	 'groupe' : '33'
	},

	{'nip' : '17796904',
	 'nom' : 'BENAZZI',
	 'prenom' : 'CHOUAIB',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '19759639',
	 'nom' : 'FOUREZ',
	 'prenom' : 'EDOUARD',
	 'formation' : 'SESI',
	 'groupe' : '34'
	},

	{'nip' : '13988344',
	 'nom' : 'BAGHEZZA',
	 'prenom' : 'MORAD',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '18164638',
	 'nom' : 'BENAZZOUZ',
	 'prenom' : 'SOFIANE',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

	{'nip' : '13034034',
	 'nom' : 'NOWACZYK',
	 'prenom' : 'TIM',
	 'formation' : 'SESI',
	 'groupe' : '44'
	},

]

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
