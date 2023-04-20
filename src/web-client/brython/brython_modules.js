__BRYTHON__.VFS_timestamp = 1681964700227
if(typeof document !== 'undefined'){
    __BRYTHON__.brython_modules = $B.last(document.getElementsByTagName('script')).src
}
__BRYTHON__.use_VFS = true
var scripts = {"$timestamp": 1681964700227, "browser": [".py", "", [], 1], "_svg": [".js", "// creation of an HTML element\nvar $module = (function($B){\n\nvar _b_ = $B.builtins\nvar TagSum = $B.TagSum // defined in py_dom.js\n\nvar $svgNS = \"http://www.w3.org/2000/svg\"\nvar $xlinkNS = \"http://www.w3.org/1999/xlink\"\n\nfunction makeTagDict(tagName){\n    // return the dictionary for the class associated with tagName\n    var dict = $B.make_class(tagName)\n\n    dict.__init__ = function(){\n        var $ns = $B.args('__init__', 1, {self: null}, ['self'],\n            arguments, {}, 'args', 'kw'),\n            self = $ns['self'],\n            args = $ns['args']\n        if(args.length == 1){\n            var first = args[0]\n            if(_b_.isinstance(first, [_b_.str, _b_.int, _b_.float])){\n                self.appendChild(document.createTextNode(_b_.str.$factory(first)))\n            }else if(first.__class__ === TagSum){\n                for(var i = 0, len = first.children.length; i < len; i++){\n                    self.appendChild(first.children[i].elt)\n                }\n            }else{ // argument is another DOMNode instance\n                try{self.appendChild(first.elt)}\n                catch(err){throw _b_.ValueError.$factory('wrong element ' + first)}\n            }\n        }\n\n        // attributes\n        var items = _b_.list.$factory(_b_.dict.items($ns['kw']))\n        for(var i = 0, len = items.length; i < len; i++){\n            // keyword arguments\n            var arg = items[i][0],\n                value = items[i][1]\n            if(arg.toLowerCase().substr(0,2) == \"on\"){\n                // Event binding passed as argument \"onclick\", \"onfocus\"...\n                // Better use method bind of DOMNode objects\n                var js = '$B.DOMNode.bind(self,\"' +\n                    arg.toLowerCase().substr(2)\n                eval(js+'\",function(){'+value+'})')\n            }else if(arg.toLowerCase() == \"style\"){\n                $B.DOMNode.set_style(self,value)\n            }else if(arg.toLowerCase().indexOf(\"href\") !== -1){ // xlink:href\n                self.setAttributeNS( \"http://www.w3.org/1999/xlink\",\n                    \"href\",value)\n            }else{\n                if(value !== false){\n                    // option.selected=false sets it to true :-)\n                    try{\n                        arg = arg.replace('_', '-')\n                        self.setAttributeNS(null, arg, value)\n                    }catch(err){\n                        throw _b_.ValueError.$factory(\"can't set attribute \" + arg)\n                    }\n                }\n            }\n        }\n    }\n\n    dict.__mro__ = [$B.DOMNode, $B.builtins.object]\n\n    dict.__new__ = function(cls){\n        var res = $B.DOMNode.$factory(document.createElementNS($svgNS, tagName))\n        res.__class__ = cls\n        return res\n    }\n\n    dict.$factory = function(){\n        var res = $B.DOMNode.$factory(\n            document.createElementNS($svgNS, tagName))\n        res.__class__ = dict\n        // apply __init__\n        dict.__init__(res, ...arguments)\n        return res\n    }\n\n    $B.set_func_names(dict, \"browser.svg\")\n\n    return dict\n}\n\n\n// SVG\nvar $svg_tags = ['a',\n'altGlyph',\n'altGlyphDef',\n'altGlyphItem',\n'animate',\n'animateColor',\n'animateMotion',\n'animateTransform',\n'circle',\n'clipPath',\n'color_profile', // instead of color-profile\n'cursor',\n'defs',\n'desc',\n'ellipse',\n'feBlend',\n'foreignObject', //patch to enable foreign objects\n'g',\n'image',\n'line',\n'linearGradient',\n'marker',\n'mask',\n'path',\n'pattern',\n'polygon',\n'polyline',\n'radialGradient',\n'rect',\n'set',\n'stop',\n'svg',\n'text',\n'tref',\n'tspan',\n'use']\n\n// create classes\nvar obj = new Object()\nvar dicts = {}\nfor(var i = 0, len = $svg_tags.length; i < len; i++){\n    var tag = $svg_tags[i]\n    obj[tag] = makeTagDict(tag)\n}\n\nreturn obj\n})(__BRYTHON__)\n"], "sys": [".py", "\nfrom _sys import *\nimport javascript\n\n_getframe=Getframe\n\nabiflags=0\n\ndef audit(event,*args):\n ''\n pass\n \nbrython_debug_mode=__BRYTHON__.debug\n\nbase_exec_prefix=__BRYTHON__.brython_path\n\nbase_prefix=__BRYTHON__.brython_path\n\nbuiltin_module_names=__BRYTHON__.builtin_module_names\n\nbyteorder='little'\n\ndont_write_bytecode=True\n\nexec_prefix=__BRYTHON__.brython_path\n\nexecutable=__BRYTHON__.brython_path+'/brython.js'\n\nargv=[__BRYTHON__.script_path]\n\n\ndef displayhook(value):\n if value is not None :\n  stdout.write(repr(value))\n  \ndef exit(i=None ):\n raise SystemExit('')\n \nclass flag_class:\n\n def __init__(self):\n  self.debug=0\n  self.inspect=0\n  self.interactive=0\n  self.optimize=0\n  self.dont_write_bytecode=0\n  self.no_user_site=0\n  self.no_site=0\n  self.ignore_environment=0\n  self.verbose=0\n  self.bytes_warning=0\n  self.quiet=0\n  self.hash_randomization=1\n  \nflags=flag_class()\n\nclass float_info:\n mant_dig=53\n max=javascript.Number.MAX_VALUE\n min=javascript.Number.MIN_VALUE\n radix=2\n \ndef getfilesystemencoding(*args,**kw):\n ''\n\n \n return 'utf-8'\n \ndef getfilesystemencodeerrors():\n return \"utf-8\"\n \ndef getrecursionlimit():\n return 200\n \ndef intern(string):\n return string\n \nclass int_info:\n bits_per_digit=30\n sizeof_digit=4\n \nmaxsize=2 **63 -1\n\nmaxunicode=1114111\n\nplatform=\"brython\"\n\nprefix=__BRYTHON__.brython_path\n\nversion='.'.join(str(x)for x in __BRYTHON__.version_info[:3])\nversion +=\" (default, %s) \\n[Javascript 1.5] on Brython\"\\\n%__BRYTHON__.compiled_date\nhexversion=0x030800f0\n\nclass _version_info:\n\n def __init__(self,version_info):\n  self.version_info=version_info\n  self.major=version_info[0]\n  self.minor=version_info[1]\n  self.micro=version_info[2]\n  self.releaselevel=version_info[3]\n  self.serial=version_info[4]\n  \n def __getitem__(self,index):\n  if isinstance(self.version_info[index],list):\n   return tuple(self.version_info[index])\n  return self.version_info[index]\n  \n def hexversion(self):\n  try :\n   return '0%d0%d0%d'%(self.major,self.minor,self.micro)\n  finally :\n   return '0%d0000'%(self.major)\n   \n def __str__(self):\n  _s=\"sys.version(major=%d, minor=%d, micro=%d, releaselevel='%s', \"\\\n  \"serial=%d)\"\n  return _s %(self.major,self.minor,self.micro,\n  self.releaselevel,self.serial)\n  \n def __eq__(self,other):\n  if isinstance(other,tuple):\n   return (self.major,self.minor,self.micro)==other\n   \n  raise Error(\"Error! I don't know how to compare!\")\n  \n def __ge__(self,other):\n  if isinstance(other,tuple):\n   return (self.major,self.minor,self.micro)>=other\n   \n  raise Error(\"Error! I don't know how to compare!\")\n  \n def __gt__(self,other):\n  if isinstance(other,tuple):\n   return (self.major,self.minor,self.micro)>other\n   \n  raise Error(\"Error! I don't know how to compare!\")\n  \n def __le__(self,other):\n  if isinstance(other,tuple):\n   return (self.major,self.minor,self.micro)<=other\n   \n  raise Error(\"Error! I don't know how to compare!\")\n  \n def __lt__(self,other):\n  if isinstance(other,tuple):\n   return (self.major,self.minor,self.micro)<other\n   \n  raise Error(\"Error! I don't know how to compare!\")\n  \n def __ne__(self,other):\n  if isinstance(other,tuple):\n   return (self.major,self.minor,self.micro)!=other\n   \n  raise Error(\"Error! I don't know how to compare!\")\n  \n  \n  \nversion_info=_version_info(__BRYTHON__.version_info)\n\nclass SimpleNamespace:\n\n def __init__(self,/,**kwargs):\n  self.__dict__.update(kwargs)\n  \n def __repr__(self):\n  items=(f\"{k}={v!r}\"for k,v in self.__dict__.items())\n  return \"{}({})\".format(\"namespace\",\", \".join(items))\n  \n def __eq__(self,other):\n  if isinstance(self,SimpleNamespace)and isinstance(other,SimpleNamespace):\n   return self.__dict__ ==other.__dict__\n  return NotImplemented\n  \nSimpleNamespace.__module__=\"types\"\n\nvi=_version_info(__BRYTHON__.implementation)\nimplementation=SimpleNamespace(name=\"brython\",\nversion=vi,\nhexversion=vi.hexversion(),\ncache_tag=None )\n\nclass _hash_info:\n\n def __init__(self):\n  self.width=32\n  self.modulus=2147483647\n  self.inf=314159\n  self.nan=0\n  self.imag=1000003\n  self.algorithm='siphash24'\n  self.hash_bits=64\n  self.seed_bits=128\n  cutoff=0\n  \n def __repr__(self):\n \n  return \"sys.hash_info(width=32, modulus=2147483647, inf=314159, \"\\\n  \"nan=0, imag=1000003, algorithm='siphash24', hash_bits=64, \"\\\n  \"seed_bits=128, cutoff=0)\"\n  \nhash_info=_hash_info()\n\nclass _float_info:\n ''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n \n def __init__(self):\n  self.dig=15\n  self.epsilon=2 **-52\n  self.mant_dig=53\n  self.max=__BRYTHON__.max_float\n  self.max_exp=2 **10\n  self.max_10_exp=308\n  self.min=2 **(-1022)\n  self.min_exp=-1021\n  self.min_10_exp=-307\n  self.radix=2\n  self.rounds=1\n  self._tuple=(self.max,self.max_exp,self.max_10_exp,self.min,\n  self.min_exp,self.min_10_exp,self.dig,self.mant_dig,self.epsilon,\n  self.radix,self.rounds)\n  \n def __getitem__(self,k):\n  return self._tuple[k]\n  \n def __iter__(self):\n  return iter(self._tuple)\n  \nfloat_info=_float_info()\n\nwarnoptions=[]\n\ndef getfilesystemencoding():\n return 'utf-8'\n \n \n__stdout__=__BRYTHON__.stdout\n__stderr__=__BRYTHON__.stderr\n__stdin__=__BRYTHON__.stdin\n\n__excepthook__=excepthook\n", ["javascript", "_sys"]], "browser.svg": [".py", "from _svg import *\n", ["_svg"]]}
__BRYTHON__.update_VFS(scripts)