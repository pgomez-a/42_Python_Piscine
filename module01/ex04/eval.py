class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        output = 0
        for coef, word in zip(coefs, words):
            output += (coef * len(word))
        return output

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        output = 0
        for coef, word in enumerate(words):
            output += (coefs[coef]  * len(word))
        return output
