# STOCKHOLM
Stockholm is a ransomware that only affects files whose extensions have been affected by **Wannacry**, inside a folder named **infection** inside **HOME** directory.

## Create and handle program

`make` Create environment and executable

`make clean` Stop environment and delete exec

## Program usage

    ./stockholm [options] KEY
				[-h|-help]
			    [-v|-version]
			    [-r|-reverse]
			    [-s|-silent] 
			    
 - **-h, -help** : display the help
 - **-v, -version**: Display program's version
 - **-r, -reverse=key**: reverse the infection using the given key
 - **-s, -silent**: Do not display the encrypted files