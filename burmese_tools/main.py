import re

class tools:
    
    @staticmethod
    def load_dict() -> dict:
        output = {'္': '်', '်': 'ျ', 'ျ': 'ြ', 'ြ': 'ွ', 'ွ': 'ှ', 'ႆ': 'ဿ', 'ဳ': 'ု', 'ဴ': 'ူ', 'ဿ': 'ူ', '၀': 'ဝ', '၎': '၎င်း', 'ၚ': 'ါ်', 'ၠ': '္က', 'ၡ': '္ခ', 'ၢ': '္ဂ', 'ၣ': '္ဃ', 'ၥ': '္စ', 'ၦ': '္ဆ', 'ၧ': '္ဆ', 'ၨ': '္ဇ', 'ၩ': '္ဈ', 'ၪ': 'ဉ', 'ၫ': 'ည', 'ၬ': '္ဋ', 'ၭ': '္ဌ', 'ၮ': 'ဍ္ဍ', 'ၯ': 'ဍ္ဎ', 'ၰ': '္ဏ', 'ၱ': '္တ', 'ၲ': '္တ', 'ၳ': '္ထ', 'ၴ': '္ထ', 'ၵ': '္ဒ', 'ၶ': '္ဓ', 'ၷ': '္န', 'ၸ': '္ပ', 'ၹ': '္ဖ', 'ၺ': '္ဗ', 'ၻ': '္ဘ', 'ၼ': '္မ', 'ၽ': 'ျ', 'ၾ': 'ြ', 'ၿ': 'ြ', 'ႀ': 'ြ', 'ႁ': 'ြ', 'ႂ': 'ြ', 'ႃ': 'ြ', 'ႄ': 'ြ', 'ႅ': '္လ', 'ႇ': 'ှ', 'ႈ': 'ှု', 'ႉ': 'ှူ', 'ႊ': 'ွှ', 'ႎ': 'ိံ', 'ႏ': 'န', '႐': 'ရ', '႑': 'ဏ္ဍ', '႒': 'ဋ္ဌ', '႓': '္ဘ', '႔': '့', '႕': '့', '႖': '္တွ', '႗': 'ဋ္ဋ', 'ၤ': 'င်္'}
        return output

    @staticmethod
    def zaw2uni(text: str) -> str:
        """
        transfrom zawgyi text to unicode text

        Args:
            text (str): zawgyi text


        Returns:
            str: unicode text
        """

        # load zaw to uni dict
        font_dictionary =  tools.load_dict()
    
        lst = list(text.strip())
        for i,char in enumerate(lst):
            if char in font_dictionary.keys():
                lst[i] = font_dictionary[char]
                
            result = ("{}"*len(lst)).format(*lst)

        # change zawgyi font order in uni code char
        uni_pattern = "(ေ)?(ြ)?([က-ဪ|ဿ-ၕ|ၚ-ၝ|ၡ|ၥ|ၦ|ၮ-ၰ|ၵ-ႁ|ႎ|႐-႙|႞|႟])(ွ)?(ှ)?(ျ)?(င်္)?(ွ)?(ှ)?(ာ)?(း)?(္က|္ခ|္ဂ|္ဃ|္စ|္ဆ|္ဇ|္ဈ|္ဋ|္ဌ|္ဏ|္တ|္ထ|္ဒ|္ဓ|္န|္ပ|္ဖ|္ဗ|္ဘ|္မ|္လ|္ဘ)?(ၘ|ၙ)?"
        result = re.sub(uni_pattern, r"\7\3\12\2\6\8\4\9\5\1\10\11\13", result)

        return result

    @staticmethod
    def uni2zaw(text: str) -> str:
        """
        transfrom unicode text to zawgyi text

        Args:
            text (str): unicode text


        Returns:
            str: zawgyi text
        """
        
        # load zaw to uni dict and split zawgyi char list and uni char list
        font_dictionary =  tools.load_dict()
        zaw_list, uni_list = list(font_dictionary.keys())[::-1], list(font_dictionary.values())[::-1] 
        
        # change unicode order to zawgyi order
        uni_pattern = "(င်္)?([က-ဪ|ဿ-ၕ|ၚ-ၝ|ၡ|ၥ|ၦ|ၮ-ၰ|ၵ-ႁ|ႎ|႐-႙|႞|႟])(္က|္ခ|္ဂ|္ဃ|္စ|္ဆ|္ဇ|္ဈ|္ဋ|္ဌ|္ဏ|္တ|္ထ|္ဒ|္ဓ|္န|္ပ|္ဖ|္ဗ|္ဘ|္မ|္လ|္ဘ)?(ြ)?(ျ)?(ွ)?(ှ)?(ေ)?(ၘ|ၙ)?"
        result = re.sub(uni_pattern, r"\8\4\2\5\1\6\7\3\9", text.strip())
        
        #change unicode char to zawgyi char
        for zaw, uni in zip(zaw_list, uni_list):
            # create unicode and zawgyi to replace
            pattern =  r"(?<!>)" + re.escape(uni) + r"(?!<)"
            replace = r">"+re.escape(zaw)+r"<"
            # replace
            result = re.sub(pattern, replace, result)

        result = re.sub(r"[><]*", "", result)
        return result

    @staticmethod
    def uni_syllable(text: str, type: int = 1, transform: bool = True) -> list:
        """
        Tokenize Unicode text into syllable tokens.

        Args:
            text (str): Unicode text to be tokenized.
            type (int, optional): Type of splitting token. Defaults to 1.
                - If `type=1`: Splits `ဂန္ဓာရ` into [`ဂ`, `န္ဓာ`, `ရ`].
                - If `type=2`: Splits `ဂန္ဓာရ` into [`ဂန္`, `ဓာ`, `ရ`].
            
            transform (bool, optional): Applies transformations like replacing `္` with `်`.
                - Only applicable if `type=2`.
                - Defaults to `True`.
            
        Returns:
            list: A list of tokenized Unicode text.
        """
        
        
        # (full (္+full)?(full+following+်)?(following)?) or (english) or (char token)
        if type == 1:
            pattern = re.compile("((?:[က-ဪ|ဿ-ၕ|ၚ-ၝ|ၡ|ၥ|ၦ|ၮ-ၰ|ၵ-ႁ|ႎ|႐-႙|႞|႟](?:္[က-ဪ|ဿ-ၕ|ၚ-ၝ|ၡ|ၥ|ၦ|ၮ-ၰ|ၵ-ႁ|ႎ|႐-႙|႞|႟])?(?:[က-ဪ|ဿ-ၕ|ၚ-ၝ|ၡ|ၥ|ၦ|ၮ-ၰ|ၵ-ႁ|ႎ|႐-႙|႞|႟][ါ-ှ|ၖ-ၙ|ၞ-ၠ|ၢ-ၤ|ၧ-ၭ|ၱ-ၴ|ႂ-ႍ|ႏ|ႚ-ႝ]*်|[ါ-ှ|ၖ-ၙ|ၞ-ၠ|ၢ-ၤ|ၧ-ၭ|ၱ-ၴ|ႂ-ႍ|ႏ|ႚ-ႝ])*)|[a-zA-Z0-9]+|.)")
            output = re.sub(pattern, r"\1 ", text)
            output = re.sub(r"\s+", " ", output)
            return output.strip().split(" ")
        
        # (full (full+following+(္|်)) or (full+following)) or (english) or (char token)
        elif type == 2:
        
            pattern = re.compile("((?:[က-ဪ|ဿ-ၕ|ၚ-ၝ|ၡ|ၥ|ၦ|ၮ-ၰ|ၵ-ႁ|ႎ|႐-႙|႞|႟](?:[က-ဪ|ဿ-ၕ|ၚ-ၝ|ၡ|ၥ|ၦ|ၮ-ၰ|ၵ-ႁ|ႎ|႐-႙|႞|႟][ါ-ှ|ၖ-ၙ|ၞ-ၠ|ၢ-ၤ|ၧ-ၭ|ၱ-ၴ|ႂ-ႍ|ႏ|ႚ-ႝ]*(္|်)|[ါ-ှ|ၖ-ၙ|ၞ-ၠ|ၢ-ၤ|ၧ-ၭ|ၱ-ၴ|ႂ-ႍ|ႏ|ႚ-ႝ])*|[a-zA-Z0-9]+|.))")
            output = re.sub(pattern, r"\1 ", text)
            output = re.sub(r"\s+", " ", output)
            
            if transform == True:
                output = re.sub("္", "်", output)
            
            return output.strip().split(" ")
    
        else:
            raise ValueError(f"Type must be 1 or 2")

    @staticmethod
    def zaw_partial_syllable(text: str) -> list:
        """
        Tokenize Zawgyi text into syllable tokens.

        Args:
            text (str): Zawgyi text to be tokenized.
            
        Returns:
            list: A list of tokenized Zawgyi text.
        """ 
        
        zaw_pattern = re.compile("((?:[ေ|ျ|ၾ-ႄ]*[က-ဪ|၀-ၕ|ၚ-ၝ|ၪ|ၮ|ၯ|ႆ|ႏ-႒|႗-႙|႞|႟][ါ-ူ|ဲ-်|ြ-ဿ|ၖ-ၙ|ၞ-ၩ|ၬ|ၭ|ၰ-ၽ|ႅ-ႎ|႓-႖|ႚ-ႝ]*)|[a-zA-Z0-9]+|.)")
        output = re.sub(zaw_pattern, r"\1 ", text)
        output = re.sub(r"\s+", " ", output)
        return output.strip().split(" ")
  