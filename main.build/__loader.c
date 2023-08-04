
/* Code to register embedded modules for meta path based loading if any. */

#include <Python.h>

/* Use a hex version of our own to compare for versions. We do not care about pre-releases */
#if PY_MICRO_VERSION < 16
#define PYTHON_VERSION (PY_MAJOR_VERSION * 256 + PY_MINOR_VERSION * 16 + PY_MICRO_VERSION)
#else
#define PYTHON_VERSION (PY_MAJOR_VERSION * 256 + PY_MINOR_VERSION * 16 + 15)
#endif

#include "nuitka/constants_blob.h"

#include "nuitka/unfreezing.h"

/* Type bool */
#ifndef __cplusplus
#include "stdbool.h"
#endif

#if 150 > 0
static unsigned char *bytecode_data[150];
#else
static unsigned char **bytecode_data = NULL;
#endif

/* Table for lookup to find compiled or bytecode modules included in this
 * binary or module, or put along this binary as extension modules. We do
 * our own loading for each of these.
 */
extern PyObject *modulecode_PIL(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$_version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_UIDIA(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_UIdialogdef(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode___main__(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode___parents_main__(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_agnes_desc(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_commands(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_dialog(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_dialogtree(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_emanuel(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_enemies(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_inventory(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jinja2(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jinja2$_identifier(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jinja2$async_utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jinja2$bccache(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jinja2$compiler(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jinja2$constants(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jinja2$debug(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jinja2$defaults(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jinja2$environment(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jinja2$exceptions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jinja2$filters(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jinja2$idtracking(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jinja2$lexer(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jinja2$loaders(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jinja2$nodes(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jinja2$optimizer(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jinja2$parser(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jinja2$runtime(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jinja2$tests(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jinja2$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jinja2$visitor(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_joseph(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_libraries(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_listbox(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_markupsafe(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_markupsafe$_native(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_multiprocessing$$45$postLoad(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_multiprocessing$$45$preLoad(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_npcdia(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_npcnames(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$__config__(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$_distributor_init(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$_globals(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$_pytesttester(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$_version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$compat(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$compat$_inspect(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$compat$py3k(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$_add_newdocs(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$_add_newdocs_scalars(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$_asarray(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$_dtype(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$_dtype_ctypes(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$_exceptions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$_internal(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$_machar(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$_methods(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$_string_helpers(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$_type_aliases(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$_ufunc_config(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$arrayprint(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$defchararray(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$einsumfunc(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$fromnumeric(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$function_base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$getlimits(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$memmap(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$multiarray(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$numeric(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$numerictypes(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$overrides(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$records(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$shape_base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$umath(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$ctypeslib(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$fft(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$fft$_pocketfft(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$fft$helper(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$_datasource(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$_iotools(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$_version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$arraypad(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$arraysetops(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$arrayterator(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$format(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$function_base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$histograms(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$index_tricks(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$mixins(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$nanfunctions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$npyio(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$polynomial(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$scimath(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$shape_base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$stride_tricks(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$twodim_base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$type_check(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$ufunclike(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$linalg(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$linalg$linalg(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$ma(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$ma$core(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$ma$extras(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$ma$mrecords(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$matrixlib(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$matrixlib$defmatrix(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$polynomial(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$polynomial$_polybase(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$polynomial$chebyshev(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$polynomial$hermite(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$polynomial$hermite_e(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$polynomial$laguerre(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$polynomial$legendre(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$polynomial$polynomial(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$polynomial$polyutils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$random(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$random$_pickle(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_paul(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pkg_resources$$45$postLoad(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_planets(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_player(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ptext(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ptexture(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$colordict(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$cursors(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$fastevent(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$ftfont(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$locals(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$macosx(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$pkgdata(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$sndarray(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$sprite(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$surfarray(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$sysfont(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$threads(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygamebutton(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_renderbase(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_slider(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_standartUIdialogref(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_terrainmask(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_terrainmask0(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_terrainmask2(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_tiledef(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_waterFX(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_xmap(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);

static struct Nuitka_MetaPathBasedLoaderEntry meta_path_loader_entries[] = {
    {"PIL", modulecode_PIL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/PIL/__init__.py"
#endif
},
    {"PIL._version", modulecode_PIL$_version, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/PIL/_version.py"
#endif
},
    {"UIDIA", modulecode_UIDIA, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/UIDIA.py"
#endif
},
    {"UIdialogdef", modulecode_UIdialogdef, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/UIdialogdef.py"
#endif
},
    {"__main__", modulecode___main__, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/main.py"
#endif
},
    {"__parents_main__", modulecode___parents_main__, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/main.py"
#endif
},
    {"_pydecimal", NULL, 0, 244244, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/_pydecimal.py"
#endif
},
    {"agnes_desc", modulecode_agnes_desc, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/agnes_desc.py"
#endif
},
    {"asyncio", NULL, 1, 1328, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/__init__.py"
#endif
},
    {"asyncio.base_events", NULL, 2, 90496, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/base_events.py"
#endif
},
    {"asyncio.base_futures", NULL, 3, 3372, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/base_futures.py"
#endif
},
    {"asyncio.base_subprocess", NULL, 4, 16687, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/base_subprocess.py"
#endif
},
    {"asyncio.base_tasks", NULL, 5, 4160, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/base_tasks.py"
#endif
},
    {"asyncio.constants", NULL, 6, 945, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/constants.py"
#endif
},
    {"asyncio.coroutines", NULL, 7, 3981, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/coroutines.py"
#endif
},
    {"asyncio.events", NULL, 8, 37771, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/events.py"
#endif
},
    {"asyncio.exceptions", NULL, 9, 3627, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/exceptions.py"
#endif
},
    {"asyncio.format_helpers", NULL, 10, 4115, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/format_helpers.py"
#endif
},
    {"asyncio.futures", NULL, 11, 18494, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/futures.py"
#endif
},
    {"asyncio.locks", NULL, 12, 29191, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/locks.py"
#endif
},
    {"asyncio.log", NULL, 13, 278, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/log.py"
#endif
},
    {"asyncio.mixins", NULL, 14, 1180, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/mixins.py"
#endif
},
    {"asyncio.protocols", NULL, 15, 9429, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/protocols.py"
#endif
},
    {"asyncio.queues", NULL, 16, 12810, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/queues.py"
#endif
},
    {"asyncio.runners", NULL, 17, 10217, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/runners.py"
#endif
},
    {"asyncio.selector_events", NULL, 18, 64166, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/selector_events.py"
#endif
},
    {"asyncio.sslproto", NULL, 19, 43500, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/sslproto.py"
#endif
},
    {"asyncio.staggered", NULL, 20, 6620, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/staggered.py"
#endif
},
    {"asyncio.streams", NULL, 21, 33661, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/streams.py"
#endif
},
    {"asyncio.subprocess", NULL, 22, 12642, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/subprocess.py"
#endif
},
    {"asyncio.taskgroups", NULL, 23, 8078, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/taskgroups.py"
#endif
},
    {"asyncio.tasks", NULL, 24, 40990, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/tasks.py"
#endif
},
    {"asyncio.threads", NULL, 25, 1277, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/threads.py"
#endif
},
    {"asyncio.timeouts", NULL, 26, 7767, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/timeouts.py"
#endif
},
    {"asyncio.transports", NULL, 27, 15153, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/transports.py"
#endif
},
    {"asyncio.trsock", NULL, 28, 5368, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/trsock.py"
#endif
},
    {"asyncio.unix_events", NULL, 29, 74362, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/asyncio/unix_events.py"
#endif
},
    {"bdb", NULL, 30, 38657, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/bdb.py"
#endif
},
    {"bz2", NULL, 31, 16146, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/bz2.py"
#endif
},
    {"commands", modulecode_commands, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/commands.py"
#endif
},
    {"concurrent", NULL, 32, 137, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/concurrent/__init__.py"
#endif
},
    {"concurrent.futures", NULL, 33, 1443, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/concurrent/futures/__init__.py"
#endif
},
    {"concurrent.futures._base", NULL, 34, 37236, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/concurrent/futures/_base.py"
#endif
},
    {"concurrent.futures.process", NULL, 35, 38006, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/concurrent/futures/process.py"
#endif
},
    {"concurrent.futures.thread", NULL, 36, 11056, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/concurrent/futures/thread.py"
#endif
},
    {"ctypes", NULL, 37, 26785, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/ctypes/__init__.py"
#endif
},
    {"ctypes._endian", NULL, 38, 3966, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/ctypes/_endian.py"
#endif
},
    {"decimal", NULL, 39, 527, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/decimal.py"
#endif
},
    {"dialog", modulecode_dialog, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/dialog.py"
#endif
},
    {"dialogtree", modulecode_dialogtree, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/dialogtree.py"
#endif
},
    {"email", NULL, 40, 2094, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/email/__init__.py"
#endif
},
    {"email._encoded_words", NULL, 41, 9101, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/email/_encoded_words.py"
#endif
},
    {"email._header_value_parser", NULL, 42, 149451, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/email/_header_value_parser.py"
#endif
},
    {"email._parseaddr", NULL, 43, 24284, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/email/_parseaddr.py"
#endif
},
    {"email._policybase", NULL, 44, 19223, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/email/_policybase.py"
#endif
},
    {"email.base64mime", NULL, 45, 4335, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/email/base64mime.py"
#endif
},
    {"email.charset", NULL, 46, 16005, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/email/charset.py"
#endif
},
    {"email.contentmanager", NULL, 47, 13814, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/email/contentmanager.py"
#endif
},
    {"email.encoders", NULL, 48, 2370, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/email/encoders.py"
#endif
},
    {"email.errors", NULL, 49, 8429, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/email/errors.py"
#endif
},
    {"email.feedparser", NULL, 50, 21447, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/email/feedparser.py"
#endif
},
    {"email.generator", NULL, 51, 21583, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/email/generator.py"
#endif
},
    {"email.header", NULL, 52, 26960, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/email/header.py"
#endif
},
    {"email.headerregistry", NULL, 53, 33737, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/email/headerregistry.py"
#endif
},
    {"email.iterators", NULL, 54, 3147, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/email/iterators.py"
#endif
},
    {"email.message", NULL, 55, 58879, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/email/message.py"
#endif
},
    {"email.parser", NULL, 56, 7368, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/email/parser.py"
#endif
},
    {"email.policy", NULL, 57, 12417, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/email/policy.py"
#endif
},
    {"email.quoprimime", NULL, 58, 11221, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/email/quoprimime.py"
#endif
},
    {"email.utils", NULL, 59, 15460, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/email/utils.py"
#endif
},
    {"emanuel", modulecode_emanuel, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/emanuel.py"
#endif
},
    {"enemies", modulecode_enemies, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/enemies.py"
#endif
},
    {"hashlib", NULL, 60, 12322, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/hashlib.py"
#endif
},
    {"hmac", NULL, 61, 11456, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/hmac.py"
#endif
},
    {"http", NULL, 62, 8717, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/http/__init__.py"
#endif
},
    {"http.client", NULL, 63, 60202, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/http/client.py"
#endif
},
    {"http.cookiejar", NULL, 64, 88127, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/http/cookiejar.py"
#endif
},
    {"inventory", modulecode_inventory, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/inventory.py"
#endif
},
    {"jinja2", modulecode_jinja2, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/jinja2/__init__.py"
#endif
},
    {"jinja2._identifier", modulecode_jinja2$_identifier, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/jinja2/_identifier.py"
#endif
},
    {"jinja2.async_utils", modulecode_jinja2$async_utils, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/jinja2/async_utils.py"
#endif
},
    {"jinja2.bccache", modulecode_jinja2$bccache, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/jinja2/bccache.py"
#endif
},
    {"jinja2.compiler", modulecode_jinja2$compiler, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/jinja2/compiler.py"
#endif
},
    {"jinja2.constants", modulecode_jinja2$constants, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/jinja2/constants.py"
#endif
},
    {"jinja2.debug", modulecode_jinja2$debug, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/jinja2/debug.py"
#endif
},
    {"jinja2.defaults", modulecode_jinja2$defaults, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/jinja2/defaults.py"
#endif
},
    {"jinja2.environment", modulecode_jinja2$environment, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/jinja2/environment.py"
#endif
},
    {"jinja2.exceptions", modulecode_jinja2$exceptions, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/jinja2/exceptions.py"
#endif
},
    {"jinja2.filters", modulecode_jinja2$filters, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/jinja2/filters.py"
#endif
},
    {"jinja2.idtracking", modulecode_jinja2$idtracking, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/jinja2/idtracking.py"
#endif
},
    {"jinja2.lexer", modulecode_jinja2$lexer, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/jinja2/lexer.py"
#endif
},
    {"jinja2.loaders", modulecode_jinja2$loaders, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/jinja2/loaders.py"
#endif
},
    {"jinja2.nodes", modulecode_jinja2$nodes, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/jinja2/nodes.py"
#endif
},
    {"jinja2.optimizer", modulecode_jinja2$optimizer, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/jinja2/optimizer.py"
#endif
},
    {"jinja2.parser", modulecode_jinja2$parser, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/jinja2/parser.py"
#endif
},
    {"jinja2.runtime", modulecode_jinja2$runtime, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/jinja2/runtime.py"
#endif
},
    {"jinja2.tests", modulecode_jinja2$tests, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/jinja2/tests.py"
#endif
},
    {"jinja2.utils", modulecode_jinja2$utils, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/jinja2/utils.py"
#endif
},
    {"jinja2.visitor", modulecode_jinja2$visitor, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/jinja2/visitor.py"
#endif
},
    {"joseph", modulecode_joseph, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/joseph.py"
#endif
},
    {"libraries", modulecode_libraries, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/libraries.py"
#endif
},
    {"listbox", modulecode_listbox, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/listbox.py"
#endif
},
    {"logging", NULL, 65, 98860, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/logging/__init__.py"
#endif
},
    {"lzma", NULL, 66, 16703, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/lzma.py"
#endif
},
    {"markupsafe", modulecode_markupsafe, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/markupsafe/__init__.py"
#endif
},
    {"markupsafe._native", modulecode_markupsafe$_native, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/markupsafe/_native.py"
#endif
},
    {"multiprocessing", NULL, 67, 1095, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/multiprocessing/__init__.py"
#endif
},
    {"multiprocessing-postLoad", modulecode_multiprocessing$$45$postLoad, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/multiprocessing/multiprocessing-postLoad.py"
#endif
},
    {"multiprocessing-preLoad", modulecode_multiprocessing$$45$preLoad, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/multiprocessing/multiprocessing-preLoad.py"
#endif
},
    {"multiprocessing.connection", NULL, 68, 48493, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/multiprocessing/connection.py"
#endif
},
    {"multiprocessing.context", NULL, 69, 19539, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/multiprocessing/context.py"
#endif
},
    {"multiprocessing.dummy", NULL, 70, 6224, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/multiprocessing/dummy/__init__.py"
#endif
},
    {"multiprocessing.dummy.connection", NULL, 71, 3959, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/multiprocessing/dummy/connection.py"
#endif
},
    {"multiprocessing.forkserver", NULL, 72, 17015, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/multiprocessing/forkserver.py"
#endif
},
    {"multiprocessing.heap", NULL, 73, 14668, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/multiprocessing/heap.py"
#endif
},
    {"multiprocessing.managers", NULL, 74, 73515, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/multiprocessing/managers.py"
#endif
},
    {"multiprocessing.pool", NULL, 75, 47352, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/multiprocessing/pool.py"
#endif
},
    {"multiprocessing.popen_fork", NULL, 76, 4345, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/multiprocessing/popen_fork.py"
#endif
},
    {"multiprocessing.popen_forkserver", NULL, 77, 4324, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/multiprocessing/popen_forkserver.py"
#endif
},
    {"multiprocessing.popen_spawn_posix", NULL, 78, 4401, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/multiprocessing/popen_spawn_posix.py"
#endif
},
    {"multiprocessing.process", NULL, 79, 19154, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/multiprocessing/process.py"
#endif
},
    {"multiprocessing.queues", NULL, 80, 19986, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/multiprocessing/queues.py"
#endif
},
    {"multiprocessing.reduction", NULL, 81, 14967, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/multiprocessing/reduction.py"
#endif
},
    {"multiprocessing.resource_sharer", NULL, 82, 9965, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/multiprocessing/resource_sharer.py"
#endif
},
    {"multiprocessing.resource_tracker", NULL, 83, 11395, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/multiprocessing/resource_tracker.py"
#endif
},
    {"multiprocessing.shared_memory", NULL, 84, 24526, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/multiprocessing/shared_memory.py"
#endif
},
    {"multiprocessing.sharedctypes", NULL, 85, 12050, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/multiprocessing/sharedctypes.py"
#endif
},
    {"multiprocessing.spawn", NULL, 86, 12509, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/multiprocessing/spawn.py"
#endif
},
    {"multiprocessing.synchronize", NULL, 87, 22158, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/multiprocessing/synchronize.py"
#endif
},
    {"multiprocessing.util", NULL, 88, 20367, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/multiprocessing/util.py"
#endif
},
    {"npcdia", modulecode_npcdia, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/npcdia.py"
#endif
},
    {"npcnames", modulecode_npcnames, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/npcnames.py"
#endif
},
    {"numpy", modulecode_numpy, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/__init__.py"
#endif
},
    {"numpy.__config__", modulecode_numpy$__config__, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/__config__.py"
#endif
},
    {"numpy._distributor_init", modulecode_numpy$_distributor_init, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/_distributor_init.py"
#endif
},
    {"numpy._globals", modulecode_numpy$_globals, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/_globals.py"
#endif
},
    {"numpy._pytesttester", modulecode_numpy$_pytesttester, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/_pytesttester.py"
#endif
},
    {"numpy._version", modulecode_numpy$_version, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/_version.py"
#endif
},
    {"numpy.compat", modulecode_numpy$compat, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/compat/__init__.py"
#endif
},
    {"numpy.compat._inspect", modulecode_numpy$compat$_inspect, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/compat/_inspect.py"
#endif
},
    {"numpy.compat.py3k", modulecode_numpy$compat$py3k, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/compat/py3k.py"
#endif
},
    {"numpy.core", modulecode_numpy$core, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/__init__.py"
#endif
},
    {"numpy.core._add_newdocs", modulecode_numpy$core$_add_newdocs, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/_add_newdocs.py"
#endif
},
    {"numpy.core._add_newdocs_scalars", modulecode_numpy$core$_add_newdocs_scalars, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/_add_newdocs_scalars.py"
#endif
},
    {"numpy.core._asarray", modulecode_numpy$core$_asarray, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/_asarray.py"
#endif
},
    {"numpy.core._dtype", modulecode_numpy$core$_dtype, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/_dtype.py"
#endif
},
    {"numpy.core._dtype_ctypes", modulecode_numpy$core$_dtype_ctypes, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/_dtype_ctypes.py"
#endif
},
    {"numpy.core._exceptions", modulecode_numpy$core$_exceptions, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/_exceptions.py"
#endif
},
    {"numpy.core._internal", modulecode_numpy$core$_internal, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/_internal.py"
#endif
},
    {"numpy.core._machar", modulecode_numpy$core$_machar, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/_machar.py"
#endif
},
    {"numpy.core._methods", modulecode_numpy$core$_methods, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/_methods.py"
#endif
},
    {"numpy.core._string_helpers", modulecode_numpy$core$_string_helpers, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/_string_helpers.py"
#endif
},
    {"numpy.core._type_aliases", modulecode_numpy$core$_type_aliases, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/_type_aliases.py"
#endif
},
    {"numpy.core._ufunc_config", modulecode_numpy$core$_ufunc_config, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/_ufunc_config.py"
#endif
},
    {"numpy.core.arrayprint", modulecode_numpy$core$arrayprint, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/arrayprint.py"
#endif
},
    {"numpy.core.defchararray", modulecode_numpy$core$defchararray, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/defchararray.py"
#endif
},
    {"numpy.core.einsumfunc", modulecode_numpy$core$einsumfunc, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/einsumfunc.py"
#endif
},
    {"numpy.core.fromnumeric", modulecode_numpy$core$fromnumeric, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/fromnumeric.py"
#endif
},
    {"numpy.core.function_base", modulecode_numpy$core$function_base, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/function_base.py"
#endif
},
    {"numpy.core.getlimits", modulecode_numpy$core$getlimits, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/getlimits.py"
#endif
},
    {"numpy.core.memmap", modulecode_numpy$core$memmap, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/memmap.py"
#endif
},
    {"numpy.core.multiarray", modulecode_numpy$core$multiarray, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/multiarray.py"
#endif
},
    {"numpy.core.numeric", modulecode_numpy$core$numeric, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/numeric.py"
#endif
},
    {"numpy.core.numerictypes", modulecode_numpy$core$numerictypes, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/numerictypes.py"
#endif
},
    {"numpy.core.overrides", modulecode_numpy$core$overrides, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/overrides.py"
#endif
},
    {"numpy.core.records", modulecode_numpy$core$records, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/records.py"
#endif
},
    {"numpy.core.shape_base", modulecode_numpy$core$shape_base, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/shape_base.py"
#endif
},
    {"numpy.core.umath", modulecode_numpy$core$umath, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/core/umath.py"
#endif
},
    {"numpy.ctypeslib", modulecode_numpy$ctypeslib, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/ctypeslib.py"
#endif
},
    {"numpy.fft", modulecode_numpy$fft, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/fft/__init__.py"
#endif
},
    {"numpy.fft._pocketfft", modulecode_numpy$fft$_pocketfft, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/fft/_pocketfft.py"
#endif
},
    {"numpy.fft.helper", modulecode_numpy$fft$helper, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/fft/helper.py"
#endif
},
    {"numpy.lib", modulecode_numpy$lib, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/lib/__init__.py"
#endif
},
    {"numpy.lib._datasource", modulecode_numpy$lib$_datasource, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/lib/_datasource.py"
#endif
},
    {"numpy.lib._iotools", modulecode_numpy$lib$_iotools, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/lib/_iotools.py"
#endif
},
    {"numpy.lib._version", modulecode_numpy$lib$_version, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/lib/_version.py"
#endif
},
    {"numpy.lib.arraypad", modulecode_numpy$lib$arraypad, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/lib/arraypad.py"
#endif
},
    {"numpy.lib.arraysetops", modulecode_numpy$lib$arraysetops, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/lib/arraysetops.py"
#endif
},
    {"numpy.lib.arrayterator", modulecode_numpy$lib$arrayterator, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/lib/arrayterator.py"
#endif
},
    {"numpy.lib.format", modulecode_numpy$lib$format, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/lib/format.py"
#endif
},
    {"numpy.lib.function_base", modulecode_numpy$lib$function_base, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/lib/function_base.py"
#endif
},
    {"numpy.lib.histograms", modulecode_numpy$lib$histograms, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/lib/histograms.py"
#endif
},
    {"numpy.lib.index_tricks", modulecode_numpy$lib$index_tricks, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/lib/index_tricks.py"
#endif
},
    {"numpy.lib.mixins", modulecode_numpy$lib$mixins, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/lib/mixins.py"
#endif
},
    {"numpy.lib.nanfunctions", modulecode_numpy$lib$nanfunctions, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/lib/nanfunctions.py"
#endif
},
    {"numpy.lib.npyio", modulecode_numpy$lib$npyio, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/lib/npyio.py"
#endif
},
    {"numpy.lib.polynomial", modulecode_numpy$lib$polynomial, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/lib/polynomial.py"
#endif
},
    {"numpy.lib.scimath", modulecode_numpy$lib$scimath, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/lib/scimath.py"
#endif
},
    {"numpy.lib.shape_base", modulecode_numpy$lib$shape_base, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/lib/shape_base.py"
#endif
},
    {"numpy.lib.stride_tricks", modulecode_numpy$lib$stride_tricks, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/lib/stride_tricks.py"
#endif
},
    {"numpy.lib.twodim_base", modulecode_numpy$lib$twodim_base, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/lib/twodim_base.py"
#endif
},
    {"numpy.lib.type_check", modulecode_numpy$lib$type_check, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/lib/type_check.py"
#endif
},
    {"numpy.lib.ufunclike", modulecode_numpy$lib$ufunclike, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/lib/ufunclike.py"
#endif
},
    {"numpy.lib.utils", modulecode_numpy$lib$utils, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/lib/utils.py"
#endif
},
    {"numpy.linalg", modulecode_numpy$linalg, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/linalg/__init__.py"
#endif
},
    {"numpy.linalg.linalg", modulecode_numpy$linalg$linalg, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/linalg/linalg.py"
#endif
},
    {"numpy.ma", modulecode_numpy$ma, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/ma/__init__.py"
#endif
},
    {"numpy.ma.core", modulecode_numpy$ma$core, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/ma/core.py"
#endif
},
    {"numpy.ma.extras", modulecode_numpy$ma$extras, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/ma/extras.py"
#endif
},
    {"numpy.ma.mrecords", modulecode_numpy$ma$mrecords, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/ma/mrecords.py"
#endif
},
    {"numpy.matrixlib", modulecode_numpy$matrixlib, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/matrixlib/__init__.py"
#endif
},
    {"numpy.matrixlib.defmatrix", modulecode_numpy$matrixlib$defmatrix, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/matrixlib/defmatrix.py"
#endif
},
    {"numpy.polynomial", modulecode_numpy$polynomial, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/polynomial/__init__.py"
#endif
},
    {"numpy.polynomial._polybase", modulecode_numpy$polynomial$_polybase, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/polynomial/_polybase.py"
#endif
},
    {"numpy.polynomial.chebyshev", modulecode_numpy$polynomial$chebyshev, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/polynomial/chebyshev.py"
#endif
},
    {"numpy.polynomial.hermite", modulecode_numpy$polynomial$hermite, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/polynomial/hermite.py"
#endif
},
    {"numpy.polynomial.hermite_e", modulecode_numpy$polynomial$hermite_e, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/polynomial/hermite_e.py"
#endif
},
    {"numpy.polynomial.laguerre", modulecode_numpy$polynomial$laguerre, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/polynomial/laguerre.py"
#endif
},
    {"numpy.polynomial.legendre", modulecode_numpy$polynomial$legendre, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/polynomial/legendre.py"
#endif
},
    {"numpy.polynomial.polynomial", modulecode_numpy$polynomial$polynomial, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/polynomial/polynomial.py"
#endif
},
    {"numpy.polynomial.polyutils", modulecode_numpy$polynomial$polyutils, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/polynomial/polyutils.py"
#endif
},
    {"numpy.random", modulecode_numpy$random, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/random/__init__.py"
#endif
},
    {"numpy.random._pickle", modulecode_numpy$random$_pickle, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/random/_pickle.py"
#endif
},
    {"numpy.testing", NULL, 89, 3934, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/testing/__init__.py"
#endif
},
    {"numpy.version", modulecode_numpy$version, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/numpy/version.py"
#endif
},
    {"paul", modulecode_paul, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/paul.py"
#endif
},
    {"pdb", NULL, 90, 85352, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/pdb.py"
#endif
},
    {"pkg_resources", NULL, 91, 159318, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/__init__.py"
#endif
},
    {"pkg_resources-postLoad", modulecode_pkg_resources$$45$postLoad, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/pkg_resources-postLoad.py"
#endif
},
    {"pkg_resources._vendor", NULL, 92, 160, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/__init__.py"
#endif
},
    {"pkg_resources._vendor.appdirs", NULL, 93, 29370, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/appdirs.py"
#endif
},
    {"pkg_resources._vendor.importlib_resources", NULL, 94, 794, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/__init__.py"
#endif
},
    {"pkg_resources._vendor.importlib_resources._adapters", NULL, 95, 10711, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/_adapters.py"
#endif
},
    {"pkg_resources._vendor.importlib_resources._common", NULL, 96, 4238, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/_common.py"
#endif
},
    {"pkg_resources._vendor.importlib_resources._compat", NULL, 97, 5523, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/_compat.py"
#endif
},
    {"pkg_resources._vendor.importlib_resources._itertools", NULL, 98, 1356, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/_itertools.py"
#endif
},
    {"pkg_resources._vendor.importlib_resources._legacy", NULL, 99, 6454, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/_legacy.py"
#endif
},
    {"pkg_resources._vendor.importlib_resources.abc", NULL, 100, 7455, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/abc.py"
#endif
},
    {"pkg_resources._vendor.importlib_resources.readers", NULL, 101, 8329, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/importlib_resources/readers.py"
#endif
},
    {"pkg_resources._vendor.jaraco", NULL, 102, 167, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/jaraco/__init__.py"
#endif
},
    {"pkg_resources._vendor.jaraco.context", NULL, 103, 9390, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/jaraco/context.py"
#endif
},
    {"pkg_resources._vendor.jaraco.functools", NULL, 104, 20253, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/jaraco/functools.py"
#endif
},
    {"pkg_resources._vendor.jaraco.text", NULL, 105, 26570, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/jaraco/text/__init__.py"
#endif
},
    {"pkg_resources._vendor.more_itertools", NULL, 106, 261, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/more_itertools/__init__.py"
#endif
},
    {"pkg_resources._vendor.more_itertools.more", NULL, 107, 167922, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/more_itertools/more.py"
#endif
},
    {"pkg_resources._vendor.more_itertools.recipes", NULL, 108, 26913, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/more_itertools/recipes.py"
#endif
},
    {"pkg_resources._vendor.packaging", NULL, 109, 532, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__init__.py"
#endif
},
    {"pkg_resources._vendor.packaging.__about__", NULL, 110, 611, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/__about__.py"
#endif
},
    {"pkg_resources._vendor.packaging._manylinux", NULL, 111, 13198, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/_manylinux.py"
#endif
},
    {"pkg_resources._vendor.packaging._musllinux", NULL, 112, 7966, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/_musllinux.py"
#endif
},
    {"pkg_resources._vendor.packaging._structures", NULL, 113, 3654, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/_structures.py"
#endif
},
    {"pkg_resources._vendor.packaging.markers", NULL, 114, 16503, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/markers.py"
#endif
},
    {"pkg_resources._vendor.packaging.requirements", NULL, 115, 7618, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/requirements.py"
#endif
},
    {"pkg_resources._vendor.packaging.specifiers", NULL, 116, 34332, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/specifiers.py"
#endif
},
    {"pkg_resources._vendor.packaging.tags", NULL, 117, 21317, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/tags.py"
#endif
},
    {"pkg_resources._vendor.packaging.utils", NULL, 118, 6652, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/utils.py"
#endif
},
    {"pkg_resources._vendor.packaging.version", NULL, 119, 21844, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/packaging/version.py"
#endif
},
    {"pkg_resources._vendor.pyparsing", NULL, 120, 8305, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/__init__.py"
#endif
},
    {"pkg_resources._vendor.pyparsing.actions", NULL, 121, 8431, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/actions.py"
#endif
},
    {"pkg_resources._vendor.pyparsing.common", NULL, 122, 14753, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/common.py"
#endif
},
    {"pkg_resources._vendor.pyparsing.core", NULL, 123, 277605, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/core.py"
#endif
},
    {"pkg_resources._vendor.pyparsing.diagram", NULL, 124, 27968, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/diagram/__init__.py"
#endif
},
    {"pkg_resources._vendor.pyparsing.exceptions", NULL, 125, 12895, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/exceptions.py"
#endif
},
    {"pkg_resources._vendor.pyparsing.helpers", NULL, 126, 53596, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/helpers.py"
#endif
},
    {"pkg_resources._vendor.pyparsing.results", NULL, 127, 36279, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/results.py"
#endif
},
    {"pkg_resources._vendor.pyparsing.testing", NULL, 128, 19475, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/testing.py"
#endif
},
    {"pkg_resources._vendor.pyparsing.unicode", NULL, 129, 15333, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/unicode.py"
#endif
},
    {"pkg_resources._vendor.pyparsing.util", NULL, 130, 14232, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/_vendor/pyparsing/util.py"
#endif
},
    {"pkg_resources.extern", NULL, 131, 4279, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib/python3.11/site-packages/pkg_resources/extern/__init__.py"
#endif
},
    {"planets", modulecode_planets, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/planets.py"
#endif
},
    {"player", modulecode_player, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/player.py"
#endif
},
    {"ptext", modulecode_ptext, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/ptext.py"
#endif
},
    {"ptexture", modulecode_ptexture, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/ptexture.py"
#endif
},
    {"pygame", modulecode_pygame, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/pygame/__init__.py"
#endif
},
    {"pygame.colordict", modulecode_pygame$colordict, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/pygame/colordict.py"
#endif
},
    {"pygame.cursors", modulecode_pygame$cursors, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/pygame/cursors.py"
#endif
},
    {"pygame.fastevent", modulecode_pygame$fastevent, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/pygame/fastevent.py"
#endif
},
    {"pygame.ftfont", modulecode_pygame$ftfont, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/pygame/ftfont.py"
#endif
},
    {"pygame.locals", modulecode_pygame$locals, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/pygame/locals.py"
#endif
},
    {"pygame.macosx", modulecode_pygame$macosx, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/pygame/macosx.py"
#endif
},
    {"pygame.pkgdata", modulecode_pygame$pkgdata, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/pygame/pkgdata.py"
#endif
},
    {"pygame.sndarray", modulecode_pygame$sndarray, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/pygame/sndarray.py"
#endif
},
    {"pygame.sprite", modulecode_pygame$sprite, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/pygame/sprite.py"
#endif
},
    {"pygame.surfarray", modulecode_pygame$surfarray, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/pygame/surfarray.py"
#endif
},
    {"pygame.sysfont", modulecode_pygame$sysfont, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/pygame/sysfont.py"
#endif
},
    {"pygame.threads", modulecode_pygame$threads, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/pygame/threads/__init__.py"
#endif
},
    {"pygame.version", modulecode_pygame$version, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site-packages/pygame/version.py"
#endif
},
    {"pygamebutton", modulecode_pygamebutton, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/pygamebutton.py"
#endif
},
    {"queue", NULL, 132, 16439, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/queue.py"
#endif
},
    {"renderbase", modulecode_renderbase, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/renderbase.py"
#endif
},
    {"runpy", NULL, 133, 16102, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/runpy.py"
#endif
},
    {"secrets", NULL, 134, 2848, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/secrets.py"
#endif
},
    {"selectors", NULL, 135, 28331, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/selectors.py"
#endif
},
    {"site", NULL, 136, 30144, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/site.py"
#endif
},
    {"slider", modulecode_slider, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/slider.py"
#endif
},
    {"socket", NULL, 137, 45463, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/socket.py"
#endif
},
    {"ssl", NULL, 138, 72345, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/ssl.py"
#endif
},
    {"standartUIdialogref", modulecode_standartUIdialogref, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/standartUIdialogref.py"
#endif
},
    {"subprocess", NULL, 139, 84666, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/subprocess.py"
#endif
},
    {"terrainmask", modulecode_terrainmask, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/terrainmask.py"
#endif
},
    {"terrainmask0", modulecode_terrainmask0, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/terrainmask0.py"
#endif
},
    {"terrainmask2", modulecode_terrainmask2, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/terrainmask2.py"
#endif
},
    {"tiledef", modulecode_tiledef, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/tiledef.py"
#endif
},
    {"urllib", NULL, 140, 133, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/urllib/__init__.py"
#endif
},
    {"urllib.error", NULL, 141, 3868, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/urllib/error.py"
#endif
},
    {"urllib.parse", NULL, 142, 54575, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/urllib/parse.py"
#endif
},
    {"urllib.request", NULL, 143, 126708, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/urllib/request.py"
#endif
},
    {"urllib.response", NULL, 144, 5176, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/urllib/response.py"
#endif
},
    {"waterFX", modulecode_waterFX, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/waterFX.py"
#endif
},
    {"xmap", modulecode_xmap, 0, 0, NUITKA_TRANSLATED_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/home/celleron56/dev/pokethemoonforautism/xmap.py"
#endif
},
    {"xml", NULL, 145, 710, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/xml/__init__.py"
#endif
},
    {"xml.parsers", NULL, 146, 320, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/xml/parsers/__init__.py"
#endif
},
    {"xml.parsers.expat", NULL, 147, 402, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/xml/parsers/expat.py"
#endif
},
    {"xmlrpc", NULL, 148, 133, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/xmlrpc/__init__.py"
#endif
},
    {"xmlrpc.client", NULL, 149, 56935, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG
#if defined(_NUITKA_FREEZER_HAS_FILE_PATH)
, "/usr/lib64/python3.11/xmlrpc/client.py"
#endif
},
    {NULL, NULL, 0, 0, 0}
};

static void _loadBytesCodesBlob(void) {
    static bool init_done = false;

    if (init_done == false) {
        loadConstantsBlob((PyObject **)bytecode_data, ".bytecode");

        init_done = true;
    }
}


void setupMetaPathBasedLoader(void) {
    static bool init_done = false;
    if (init_done == false) {
        _loadBytesCodesBlob();
        registerMetaPathBasedUnfreezer(meta_path_loader_entries, bytecode_data);

        init_done = true;
    }
}

// This provides the frozen (compiled bytecode) files that are included if
// any.

// These modules should be loaded as bytecode. They may e.g. have to be loadable
// during "Py_Initialize" already, or for irrelevance, they are only included
// in this un-optimized form. These are not compiled by Nuitka, and therefore
// are not accelerated at all, merely bundled with the binary or module, so
// that CPython library can start out finding them.

struct frozen_desc {
    char const *name;
    int index;
    int size;
};

static struct frozen_desc _frozen_modules[] = {

    {NULL, 0, 0}
};


void copyFrozenModulesTo(struct _frozen *destination) {
    _loadBytesCodesBlob();

    struct frozen_desc *current = _frozen_modules;

    for (;;) {
        destination->name = (char *)current->name;
        destination->code = bytecode_data[current->index];
        destination->size = current->size;
#if PYTHON_VERSION >= 0x3b0
        destination->is_package = current->size < 0;
        destination->size = Py_ABS(destination->size);
        destination->get_code = NULL;
#endif
        if (destination->name == NULL) break;

        current += 1;
        destination += 1;
    };
}

