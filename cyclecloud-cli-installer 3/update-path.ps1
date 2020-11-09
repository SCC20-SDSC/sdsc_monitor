$ErrorActionPreference = "Stop"

function add-folder-to-path($target, $folder) {
    $OldPath = [System.Environment]::GetEnvironmentVariable("path", $target)
    $NewPath = $OldPath
    if (!$NewPath.EndsWith(";")) {
        $NewPath += ";"
    }
    $NewPath += "$folder;"

    [System.Environment]::SetEnvironmentVariable("path", $NewPath, $target)
}

$t = $args[0]
$f = $args[1]

if (!("$env:Path".Split(";").Contains($f))) {
    echo "Adding '$f' to your $t path." 
    add-folder-to-path "$t" "$f"
}
