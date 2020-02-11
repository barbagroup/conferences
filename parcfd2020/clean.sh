#!/usr/bin/env bash
# Clean folder of LaTeX-generated files.

scriptdir="$( cd "$(dirname "$0")" ; pwd -P )"
cd $scriptdir

rm -f *.aux *.bbl *.blg *.fdb_latexmk *.fls *.log *.synctex.gz

