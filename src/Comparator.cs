using System.Diagnostics;
using System.IO;

namespace Tools
{
    class Comparator
    {
        public static bool Compare(string executable, string leftImgPath, string rightImgPath, out float degree)
        {
            degree = 0f;

            if (string.IsNullOrEmpty(leftImgPath) || !File.Exists(leftImgPath)
                || string.IsNullOrEmpty(rightImgPath) || !File.Exists(rightImgPath))
                return false;

            var process = new Process();

            var startInfo = new ProcessStartInfo(executable, $"{leftImgPath} {rightImgPath}");
            startInfo.UseShellExecute = false;
            startInfo.CreateNoWindow = true;
            startInfo.RedirectStandardOutput = true;
            process.StartInfo = startInfo;

            var output = "";

            process.OutputDataReceived += (sender, e) =>
            {
                if (e.Data != null)
                    output += e.Data;
            };

            process.Start();
            process.BeginOutputReadLine();

            return float.TryParse(output, out degree);
        }
    }
}
