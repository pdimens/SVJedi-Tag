#!/usr/bin/env python3

#*****************************************************************************
#  Name: SVJedi-Tag
#  Description: Genotyping of SVs with linked-reads data
#  Copyright (C) 2025 INRIA
#  Author: Anne Guichard, Mélody Temperville
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#*****************************************************************************
import argparse
from . import run, predict_genotype

def build_parser():
    parser = argparse.ArgumentParser(prog="svjedi-tag")
    subparsers = parser.add_subparsers(required=True)
    run.add_subparser(subparsers)
    predict.add_subparser(subparsers)
    return parser

def main():
    args = build_parser().parse_args()
    args.func(args)

if __name__ == "__main__":
    main()