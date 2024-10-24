
# Language extension
from enum import Enum

# List of popular languages constant and display name
class Language(Enum):
    Python = 'Python'
    JavaScript = 'JavaScript'
    Java = 'Java'
    CSharp = 'C#'
    CPlusPlus = 'C++'
    C = 'C'
    PHP = 'PHP'
    Swift = 'Swift'
    Go = 'Go'
    Ruby = 'Ruby'
    Kotlin = 'Kotlin'
    Rust = 'Rust'
    TypeScript = 'TypeScript'
    SQL = 'SQL'
    Shell = 'Shell'
    R = 'R'
    Scala = 'Scala'
    ObjectiveC = 'Objective-C'
    Perl = 'Perl'
    Dart = 'Dart'
    Elixir = 'Elixir'
    Haskell = 'Haskell'
    Lua = 'Lua'
    MATLAB = 'MATLAB'
    Erlang = 'Erlang'
    FSharp = 'FSharp'
    VBA = 'VBA'
    Groovy = 'Groovy'
    VisualBasicNET = 'Visual Basic .NET'
    Assembly = 'Assembly'


# List of popular language and it file extension.
LANGUAGE_EXTENTIONS = {
    Language.Python: 'py',
    Language.JavaScript: 'js',
    Language.Java: 'java',
    Language.CSharp: 'cs',
    Language.CPlusPlus: ['cpp', 'h', 'hpp'],
    Language.C: ['c', 'h'],
    Language.PHP: 'php',
    Language.Swift: 'swift',
    Language.Go: 'go',
    Language.Ruby: 'rb',
    Language.Kotlin: 'kt',
    Language.Rust: 'rs',
    Language.TypeScript: 'ts',
    Language.SQL: 'sql',
    Language.Shell: 'sh',
    Language.R: 'r',
    Language.Scala: 'scala',
    Language.ObjectiveC: ['m', 'h'],
    Language.Perl: 'pl',
    Language.Dart: 'dart',
    Language.Elixir: ['ex', 'exs'],
    Language.Haskell: 'hs',
    Language.Lua: 'lua',
    Language.MATLAB: 'm',
    Language.Erlang: ['erl', 'hrl'],
    Language.FSharp: ['fs', 'fsi', 'fsx'],
    Language.VBA: ['vba', 'bas'],
    Language.Groovy: 'groovy',
    Language.VisualBasicNET: 'vb',
    Language.Assembly: ['asm', 's', 'a'],
}


def get_extensions():
    """
    Get all language extensions.
    :returns: list of all extensions.
    """
    extensions = []
    for v in LANGUAGE_EXTENTIONS.values():
        extensions.extend(v if isinstance(v, list) else [v])
    return extensions


def language_from_extension(ext:str):
    """
    Get language from extension.
    :param str: langextension
    :returns: Language enum.
    :rtype Language:
    """
    for lang in LANGUAGE_EXTENTIONS:
        if ext == LANGUAGE_EXTENTIONS[lang] or ext in LANGUAGE_EXTENTIONS[lang]:
            return lang

