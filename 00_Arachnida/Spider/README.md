# SPIDER
The spider program allow you to extract all the images from a website, recursively, by providing an URL as a parameter.

## Setup

`make` Create environment and executable

`make clean` stop environment and delete exec

## Usage
    ./spider [-rlp] URL

 - Option -r : recursively downloads the images in a URL received as a  parameter. 
  - Option -r -l [N] : indicates the maximum depth level of
   the recursive download. If not indicated, it will be 5. 
  - Option -p   [PATH] : indicates the path where the downloaded files will be saved.
   *If not specified, ./data/ will be used.*