# FFUF

Fast web fuzzer ffuf is a versatile command-line tool used for web fuzzing. It is designed to make web fuzzing easier and more effective by providing a range of features and options that allow you to customize your fuzzing tasks. If you are familiar with curl, many of the command line flags of ffuf should feel familiar.

## Core Concepts

At its most basic, ffuf requires two things to run:

    1. A wordlist or a command that provides different inputs.
    2. The FUZZ keyword(s) are placed in some parts of the request.

For example:

    ```bash
    ffuf -w wordlist.txt -u 'https://ffuf.io.fi/FUZZ'
    ```

## Wordlists

Wordlists are used to provide ffuf with different inputs to test. You can supply one or more wordlists on the command line. If you are using multiple wordlists, you can configure a custom FUZZ keyword for them​1​.

## Multiple Wordlists

With ffuf, you can supply multiple wordlists. Depending on the operation mode selected, the behaviour can differ. Two notable modes are the Clusterbomb mode and the Pitchfork mode.

    - `Clusterbomb` mode: The default mode for multi-wordlists. It tests all possible combinations of the words from the wordlists​1​.
    - `Pitchfork mode`: An alternative multi-wordlist mode. The wordlists are read in lockstep, meaning the first word from all the wordlists is used in the first request, the second word for the second, and so on​1​.

## Request Configuration

`ffuf` allows for quite a few different ways to customize the request. You can supply it with a raw HTTP `-request` file, define the HTTP verb using the `-X VERBNAME` argument, and define different header key-value pairs using the `-H 'Name: Value'` argument. Moreover, you can add a request body to the request with the `-d your_request_body_here argument​1`​.

## Wordlist Resources

Here are some links to good wordlist collections:

    1. (A combination wordlist from multiple sources)[https://github.com/six2dez/OneListForAll]
    2. (Collection of context-specific wordlists)[https://github.com/danielmiessler/SecLists]

These resources should provide a solid starting point for fuzzing tasks​1​.

## Usage

For more in-depth usage and options, please refer to the [ffuf documentation](https://github.com/ffuf/ffuf/wiki).
