class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []

        for log in logs:
            identifier, rest = log.split(" ", 1)
            if rest[0].isalpha():
                letter_logs.append((rest, identifier, log))
            else:
                digit_logs.append(log)
        
        letter_logs.sort(key=lambda x: (x[0], x[1]))

        result = [log[2] for log in letter_logs] + digit_logs
        return result