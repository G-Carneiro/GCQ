#!/bin/bash

pandoc shor.rst -o shor.md
pandoc header.yaml shor.md -o shor.pdf --pdf-engine=xelatex
rm shor.md