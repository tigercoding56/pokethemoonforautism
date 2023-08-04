/* Generated code for Python module 'pygame.fastevent'
 * created by Nuitka version 1.7.7
 *
 * This code is in part copyright 2023 Kay Hayen.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "nuitka/prelude.h"

#include "nuitka/unfreezing.h"

#include "__helpers.h"

/* The "module_pygame$fastevent" is a Python object pointer of module type.
 *
 * Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_pygame$fastevent;
PyDictObject *moduledict_pygame$fastevent;

/* The declarations of module constants used, if any. */
static PyObject *mod_consts[43];
#ifndef __NUITKA_NO_ASSERT__
static Py_hash_t mod_consts_hash[43];
#endif

static PyObject *module_filename_obj = NULL;

/* Indicator if this modules private constants were created yet. */
static bool constants_created = false;

/* Function to create module private constants. */
static void createModuleConstants(void) {
    if (constants_created == false) {
        loadConstantsBlob(&mod_consts[0], UNTRANSLATE("pygame.fastevent"));
        constants_created = true;

#ifndef __NUITKA_NO_ASSERT__
        for (int i = 0; i < 43; i++) {
            mod_consts_hash[i] = DEEP_HASH(mod_consts[i]);
        }
#endif
    }
}

// We want to be able to initialize the "__main__" constants in any case.
#if 0
void createMainModuleConstants(void) {
    createModuleConstants();
}
#endif

/* Function to verify module private constants for non-corruption. */
#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants_pygame$fastevent(void) {
    // The module may not have been used at all, then ignore this.
    if (constants_created == false) return;

    for (int i = 0; i < 43; i++) {
        assert(mod_consts_hash[i] == DEEP_HASH(mod_consts[i]));
        CHECK_OBJECT_DEEP(mod_consts[i]);
    }
}
#endif

// The module code objects.
static PyCodeObject *codeobj_a44e3400414d04942b82894fd318c250;
static PyCodeObject *codeobj_c46da681bb4a310523970e77d37f20d5;
static PyCodeObject *codeobj_98250ffa89a8b9574d0d88a4ace068bd;
static PyCodeObject *codeobj_683e7017b199f468680c80589e615920;
static PyCodeObject *codeobj_7d8282e62902e59592aec14bf40e9db8;
static PyCodeObject *codeobj_f691136a0b5ae56578dda9ab384c943d;
static PyCodeObject *codeobj_a06781bb6092cb23dff445b4e77c8f52;
static PyCodeObject *codeobj_53618d9d517a863327a483b66b1ee760;
static PyCodeObject *codeobj_c5eb71e2eaf13bbf998f9edf99a14c35;
static PyCodeObject *codeobj_099b0c94f22094734376b6ea5e744ec7;

static void createModuleCodeObjects(void) {
    module_filename_obj = mod_consts[27]; CHECK_OBJECT(module_filename_obj);
    codeobj_a44e3400414d04942b82894fd318c250 = MAKE_CODE_OBJECT(module_filename_obj, 1, 0, mod_consts[40], mod_consts[40], NULL, NULL, 0, 0, 0);
    codeobj_c46da681bb4a310523970e77d37f20d5 = MAKE_CODE_OBJECT(module_filename_obj, 16, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[13], mod_consts[13], NULL, NULL, 0, 0, 0);
    codeobj_98250ffa89a8b9574d0d88a4ace068bd = MAKE_CODE_OBJECT(module_filename_obj, 24, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[10], mod_consts[10], NULL, NULL, 0, 0, 0);
    codeobj_683e7017b199f468680c80589e615920 = MAKE_CODE_OBJECT(module_filename_obj, 75, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[21], mod_consts[21], NULL, NULL, 0, 0, 0);
    codeobj_7d8282e62902e59592aec14bf40e9db8 = MAKE_CODE_OBJECT(module_filename_obj, 44, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[7], mod_consts[7], NULL, NULL, 0, 0, 0);
    codeobj_f691136a0b5ae56578dda9ab384c943d = MAKE_CODE_OBJECT(module_filename_obj, 32, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[39], mod_consts[39], NULL, NULL, 0, 0, 0);
    codeobj_a06781bb6092cb23dff445b4e77c8f52 = MAKE_CODE_OBJECT(module_filename_obj, 67, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[19], mod_consts[19], NULL, NULL, 0, 0, 0);
    codeobj_53618d9d517a863327a483b66b1ee760 = MAKE_CODE_OBJECT(module_filename_obj, 83, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[23], mod_consts[23], mod_consts[41], NULL, 1, 0, 0);
    codeobj_c5eb71e2eaf13bbf998f9edf99a14c35 = MAKE_CODE_OBJECT(module_filename_obj, 51, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[15], mod_consts[15], NULL, NULL, 0, 0, 0);
    codeobj_099b0c94f22094734376b6ea5e744ec7 = MAKE_CODE_OBJECT(module_filename_obj, 59, CO_OPTIMIZED | CO_NEWLOCALS, mod_consts[17], mod_consts[17], NULL, NULL, 0, 0, 0);
}

// The module function declarations.
static PyObject *MAKE_FUNCTION_pygame$fastevent$$$function__1__ft_init_check();


static PyObject *MAKE_FUNCTION_pygame$fastevent$$$function__2__quit_hook();


static PyObject *MAKE_FUNCTION_pygame$fastevent$$$function__3_init();


static PyObject *MAKE_FUNCTION_pygame$fastevent$$$function__4_get_init();


static PyObject *MAKE_FUNCTION_pygame$fastevent$$$function__5_pump();


static PyObject *MAKE_FUNCTION_pygame$fastevent$$$function__6_wait();


static PyObject *MAKE_FUNCTION_pygame$fastevent$$$function__7_poll();


static PyObject *MAKE_FUNCTION_pygame$fastevent$$$function__8_get();


static PyObject *MAKE_FUNCTION_pygame$fastevent$$$function__9_post(PyObject *annotations);


// The module function definitions.
static PyObject *impl_pygame$fastevent$$$function__1__ft_init_check(struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    struct Nuitka_FrameObject *frame_c46da681bb4a310523970e77d37f20d5;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    int tmp_res;
    static struct Nuitka_FrameObject *cache_frame_c46da681bb4a310523970e77d37f20d5 = NULL;
    PyObject *tmp_return_value = NULL;

    // Actual function body.
    if (isFrameUnusable(cache_frame_c46da681bb4a310523970e77d37f20d5)) {
        Py_XDECREF(cache_frame_c46da681bb4a310523970e77d37f20d5);

#if _DEBUG_REFCOUNTS
        if (cache_frame_c46da681bb4a310523970e77d37f20d5 == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_c46da681bb4a310523970e77d37f20d5 = MAKE_FUNCTION_FRAME(codeobj_c46da681bb4a310523970e77d37f20d5, module_pygame$fastevent, 0);
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }

    assert(cache_frame_c46da681bb4a310523970e77d37f20d5->m_type_description == NULL);
    frame_c46da681bb4a310523970e77d37f20d5 = cache_frame_c46da681bb4a310523970e77d37f20d5;

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStackCompiledFrame(frame_c46da681bb4a310523970e77d37f20d5);
    assert(Py_REFCNT(frame_c46da681bb4a310523970e77d37f20d5) == 2);

    // Framed code:
    {
        bool tmp_condition_result_1;
        PyObject *tmp_operand_value_1;
        tmp_operand_value_1 = GET_STRING_DICT_VALUE(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[0]);

        if (unlikely(tmp_operand_value_1 == NULL)) {
            tmp_operand_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[0]);
        }

        if (tmp_operand_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 20;

            goto frame_exception_exit_1;
        }
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_1);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 20;

            goto frame_exception_exit_1;
        }
        tmp_condition_result_1 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_1 != false) {
            goto branch_yes_1;
        } else {
            goto branch_no_1;
        }
    }
    branch_yes_1:;
    {
        PyObject *tmp_raise_type_1;
        PyObject *tmp_called_value_1;
        tmp_called_value_1 = GET_STRING_DICT_VALUE(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[1]);

        if (unlikely(tmp_called_value_1 == NULL)) {
            tmp_called_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[1]);
        }

        if (tmp_called_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 21;

            goto frame_exception_exit_1;
        }
        frame_c46da681bb4a310523970e77d37f20d5->m_frame.f_lineno = 21;
        tmp_raise_type_1 = CALL_FUNCTION_WITH_POSARGS1(tmp_called_value_1, mod_consts[2]);

        if (tmp_raise_type_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 21;

            goto frame_exception_exit_1;
        }
        exception_type = tmp_raise_type_1;
        exception_lineno = 21;
        RAISE_EXCEPTION_WITH_TYPE(&exception_type, &exception_value, &exception_tb);

        goto frame_exception_exit_1;
    }
    branch_no_1:;


    // Put the previous frame back on top.
    popFrameStack();

    goto frame_no_exception_1;
    frame_exception_exit_1:


    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_c46da681bb4a310523970e77d37f20d5, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_c46da681bb4a310523970e77d37f20d5->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_c46da681bb4a310523970e77d37f20d5, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_c46da681bb4a310523970e77d37f20d5,
        type_description_1
    );


    // Release cached frame if used for exception.
    if (frame_c46da681bb4a310523970e77d37f20d5 == cache_frame_c46da681bb4a310523970e77d37f20d5) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif
        Py_DECREF(cache_frame_c46da681bb4a310523970e77d37f20d5);
        cache_frame_c46da681bb4a310523970e77d37f20d5 = NULL;
    }

    assertFrameObject(frame_c46da681bb4a310523970e77d37f20d5);

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto function_exception_exit;
    frame_no_exception_1:;
    tmp_return_value = Py_None;
    Py_INCREF(tmp_return_value);
    goto function_return_exit;

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:

    assert(exception_type);
    RESTORE_ERROR_OCCURRED(exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.


   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !ERROR_OCCURRED());
   return tmp_return_value;
}


static PyObject *impl_pygame$fastevent$$$function__2__quit_hook(struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *tmp_return_value = NULL;

    // Actual function body.
    {
        PyObject *tmp_assign_source_1;
        tmp_assign_source_1 = Py_False;
        UPDATE_STRING_DICT0(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[0], tmp_assign_source_1);
    }
    tmp_return_value = Py_None;
    Py_INCREF(tmp_return_value);
    goto function_return_exit;

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;


function_return_exit:
   // Function cleanup code if any.


   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !ERROR_OCCURRED());
   return tmp_return_value;
}


static PyObject *impl_pygame$fastevent$$$function__3_init(struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    struct Nuitka_FrameObject *frame_f691136a0b5ae56578dda9ab384c943d;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    int tmp_res;
    NUITKA_MAY_BE_UNUSED nuitka_void tmp_unused;
    static struct Nuitka_FrameObject *cache_frame_f691136a0b5ae56578dda9ab384c943d = NULL;
    PyObject *tmp_return_value = NULL;

    // Actual function body.
    if (isFrameUnusable(cache_frame_f691136a0b5ae56578dda9ab384c943d)) {
        Py_XDECREF(cache_frame_f691136a0b5ae56578dda9ab384c943d);

#if _DEBUG_REFCOUNTS
        if (cache_frame_f691136a0b5ae56578dda9ab384c943d == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_f691136a0b5ae56578dda9ab384c943d = MAKE_FUNCTION_FRAME(codeobj_f691136a0b5ae56578dda9ab384c943d, module_pygame$fastevent, 0);
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }

    assert(cache_frame_f691136a0b5ae56578dda9ab384c943d->m_type_description == NULL);
    frame_f691136a0b5ae56578dda9ab384c943d = cache_frame_f691136a0b5ae56578dda9ab384c943d;

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStackCompiledFrame(frame_f691136a0b5ae56578dda9ab384c943d);
    assert(Py_REFCNT(frame_f691136a0b5ae56578dda9ab384c943d) == 2);

    // Framed code:
    {
        bool tmp_condition_result_1;
        PyObject *tmp_operand_value_1;
        PyObject *tmp_called_instance_1;
        PyObject *tmp_expression_value_1;
        tmp_expression_value_1 = GET_STRING_DICT_VALUE(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_1 == NULL)) {
            tmp_expression_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 37;

            goto frame_exception_exit_1;
        }
        tmp_called_instance_1 = LOOKUP_ATTRIBUTE(tmp_expression_value_1, mod_consts[6]);
        if (tmp_called_instance_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 37;

            goto frame_exception_exit_1;
        }
        frame_f691136a0b5ae56578dda9ab384c943d->m_frame.f_lineno = 37;
        tmp_operand_value_1 = CALL_METHOD_NO_ARGS(tmp_called_instance_1, mod_consts[7]);
        Py_DECREF(tmp_called_instance_1);
        if (tmp_operand_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 37;

            goto frame_exception_exit_1;
        }
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_1);
        Py_DECREF(tmp_operand_value_1);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 37;

            goto frame_exception_exit_1;
        }
        tmp_condition_result_1 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_1 != false) {
            goto branch_yes_1;
        } else {
            goto branch_no_1;
        }
    }
    branch_yes_1:;
    {
        PyObject *tmp_raise_type_1;
        PyObject *tmp_called_value_1;
        tmp_called_value_1 = GET_STRING_DICT_VALUE(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[1]);

        if (unlikely(tmp_called_value_1 == NULL)) {
            tmp_called_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[1]);
        }

        if (tmp_called_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 38;

            goto frame_exception_exit_1;
        }
        frame_f691136a0b5ae56578dda9ab384c943d->m_frame.f_lineno = 38;
        tmp_raise_type_1 = CALL_FUNCTION_WITH_POSARGS1(tmp_called_value_1, mod_consts[8]);

        if (tmp_raise_type_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 38;

            goto frame_exception_exit_1;
        }
        exception_type = tmp_raise_type_1;
        exception_lineno = 38;
        RAISE_EXCEPTION_WITH_TYPE(&exception_type, &exception_value, &exception_tb);

        goto frame_exception_exit_1;
    }
    branch_no_1:;
    {
        PyObject *tmp_called_value_2;
        PyObject *tmp_call_result_1;
        PyObject *tmp_args_element_value_1;
        tmp_called_value_2 = GET_STRING_DICT_VALUE(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[9]);

        if (unlikely(tmp_called_value_2 == NULL)) {
            tmp_called_value_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[9]);
        }

        if (tmp_called_value_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 40;

            goto frame_exception_exit_1;
        }
        tmp_args_element_value_1 = GET_STRING_DICT_VALUE(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[10]);

        if (unlikely(tmp_args_element_value_1 == NULL)) {
            tmp_args_element_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[10]);
        }

        if (tmp_args_element_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 40;

            goto frame_exception_exit_1;
        }
        frame_f691136a0b5ae56578dda9ab384c943d->m_frame.f_lineno = 40;
        tmp_call_result_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_2, tmp_args_element_value_1);
        if (tmp_call_result_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 40;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_1);
    }


    // Put the previous frame back on top.
    popFrameStack();

    goto frame_no_exception_1;
    frame_exception_exit_1:


    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_f691136a0b5ae56578dda9ab384c943d, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_f691136a0b5ae56578dda9ab384c943d->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_f691136a0b5ae56578dda9ab384c943d, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_f691136a0b5ae56578dda9ab384c943d,
        type_description_1
    );


    // Release cached frame if used for exception.
    if (frame_f691136a0b5ae56578dda9ab384c943d == cache_frame_f691136a0b5ae56578dda9ab384c943d) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif
        Py_DECREF(cache_frame_f691136a0b5ae56578dda9ab384c943d);
        cache_frame_f691136a0b5ae56578dda9ab384c943d = NULL;
    }

    assertFrameObject(frame_f691136a0b5ae56578dda9ab384c943d);

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto function_exception_exit;
    frame_no_exception_1:;
    {
        PyObject *tmp_assign_source_1;
        tmp_assign_source_1 = Py_True;
        UPDATE_STRING_DICT0(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[0], tmp_assign_source_1);
    }
    tmp_return_value = Py_None;
    Py_INCREF(tmp_return_value);
    goto function_return_exit;

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:

    assert(exception_type);
    RESTORE_ERROR_OCCURRED(exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.


   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !ERROR_OCCURRED());
   return tmp_return_value;
}


static PyObject *impl_pygame$fastevent$$$function__4_get_init(struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    struct Nuitka_FrameObject *frame_7d8282e62902e59592aec14bf40e9db8;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *tmp_return_value = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    static struct Nuitka_FrameObject *cache_frame_7d8282e62902e59592aec14bf40e9db8 = NULL;

    // Actual function body.
    if (isFrameUnusable(cache_frame_7d8282e62902e59592aec14bf40e9db8)) {
        Py_XDECREF(cache_frame_7d8282e62902e59592aec14bf40e9db8);

#if _DEBUG_REFCOUNTS
        if (cache_frame_7d8282e62902e59592aec14bf40e9db8 == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_7d8282e62902e59592aec14bf40e9db8 = MAKE_FUNCTION_FRAME(codeobj_7d8282e62902e59592aec14bf40e9db8, module_pygame$fastevent, 0);
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }

    assert(cache_frame_7d8282e62902e59592aec14bf40e9db8->m_type_description == NULL);
    frame_7d8282e62902e59592aec14bf40e9db8 = cache_frame_7d8282e62902e59592aec14bf40e9db8;

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStackCompiledFrame(frame_7d8282e62902e59592aec14bf40e9db8);
    assert(Py_REFCNT(frame_7d8282e62902e59592aec14bf40e9db8) == 2);

    // Framed code:
    tmp_return_value = GET_STRING_DICT_VALUE(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[0]);

    if (unlikely(tmp_return_value == NULL)) {
        tmp_return_value = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[0]);
    }

    if (tmp_return_value == NULL) {
        assert(ERROR_OCCURRED());

        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


        exception_lineno = 48;

        goto frame_exception_exit_1;
    }
    Py_INCREF(tmp_return_value);
    goto frame_return_exit_1;


    // Put the previous frame back on top.
    popFrameStack();

    goto frame_no_exception_1;
    frame_return_exit_1:

    // Put the previous frame back on top.
    popFrameStack();

    goto function_return_exit;
    frame_exception_exit_1:


    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_7d8282e62902e59592aec14bf40e9db8, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_7d8282e62902e59592aec14bf40e9db8->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_7d8282e62902e59592aec14bf40e9db8, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_7d8282e62902e59592aec14bf40e9db8,
        type_description_1
    );


    // Release cached frame if used for exception.
    if (frame_7d8282e62902e59592aec14bf40e9db8 == cache_frame_7d8282e62902e59592aec14bf40e9db8) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif
        Py_DECREF(cache_frame_7d8282e62902e59592aec14bf40e9db8);
        cache_frame_7d8282e62902e59592aec14bf40e9db8 = NULL;
    }

    assertFrameObject(frame_7d8282e62902e59592aec14bf40e9db8);

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto function_exception_exit;
    frame_no_exception_1:;

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:

    assert(exception_type);
    RESTORE_ERROR_OCCURRED(exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.


   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !ERROR_OCCURRED());
   return tmp_return_value;
}


static PyObject *impl_pygame$fastevent$$$function__5_pump(struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    struct Nuitka_FrameObject *frame_c5eb71e2eaf13bbf998f9edf99a14c35;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    NUITKA_MAY_BE_UNUSED nuitka_void tmp_unused;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    static struct Nuitka_FrameObject *cache_frame_c5eb71e2eaf13bbf998f9edf99a14c35 = NULL;
    PyObject *tmp_return_value = NULL;

    // Actual function body.
    if (isFrameUnusable(cache_frame_c5eb71e2eaf13bbf998f9edf99a14c35)) {
        Py_XDECREF(cache_frame_c5eb71e2eaf13bbf998f9edf99a14c35);

#if _DEBUG_REFCOUNTS
        if (cache_frame_c5eb71e2eaf13bbf998f9edf99a14c35 == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_c5eb71e2eaf13bbf998f9edf99a14c35 = MAKE_FUNCTION_FRAME(codeobj_c5eb71e2eaf13bbf998f9edf99a14c35, module_pygame$fastevent, 0);
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }

    assert(cache_frame_c5eb71e2eaf13bbf998f9edf99a14c35->m_type_description == NULL);
    frame_c5eb71e2eaf13bbf998f9edf99a14c35 = cache_frame_c5eb71e2eaf13bbf998f9edf99a14c35;

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStackCompiledFrame(frame_c5eb71e2eaf13bbf998f9edf99a14c35);
    assert(Py_REFCNT(frame_c5eb71e2eaf13bbf998f9edf99a14c35) == 2);

    // Framed code:
    {
        PyObject *tmp_called_value_1;
        PyObject *tmp_call_result_1;
        tmp_called_value_1 = GET_STRING_DICT_VALUE(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[13]);

        if (unlikely(tmp_called_value_1 == NULL)) {
            tmp_called_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[13]);
        }

        if (tmp_called_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 55;

            goto frame_exception_exit_1;
        }
        frame_c5eb71e2eaf13bbf998f9edf99a14c35->m_frame.f_lineno = 55;
        tmp_call_result_1 = CALL_FUNCTION_NO_ARGS(tmp_called_value_1);
        if (tmp_call_result_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 55;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_1);
    }
    {
        PyObject *tmp_called_instance_1;
        PyObject *tmp_expression_value_1;
        PyObject *tmp_call_result_2;
        tmp_expression_value_1 = GET_STRING_DICT_VALUE(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_1 == NULL)) {
            tmp_expression_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 56;

            goto frame_exception_exit_1;
        }
        tmp_called_instance_1 = LOOKUP_ATTRIBUTE(tmp_expression_value_1, mod_consts[14]);
        if (tmp_called_instance_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 56;

            goto frame_exception_exit_1;
        }
        frame_c5eb71e2eaf13bbf998f9edf99a14c35->m_frame.f_lineno = 56;
        tmp_call_result_2 = CALL_METHOD_NO_ARGS(tmp_called_instance_1, mod_consts[15]);
        Py_DECREF(tmp_called_instance_1);
        if (tmp_call_result_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 56;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_2);
    }


    // Put the previous frame back on top.
    popFrameStack();

    goto frame_no_exception_1;
    frame_exception_exit_1:


    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_c5eb71e2eaf13bbf998f9edf99a14c35, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_c5eb71e2eaf13bbf998f9edf99a14c35->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_c5eb71e2eaf13bbf998f9edf99a14c35, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_c5eb71e2eaf13bbf998f9edf99a14c35,
        type_description_1
    );


    // Release cached frame if used for exception.
    if (frame_c5eb71e2eaf13bbf998f9edf99a14c35 == cache_frame_c5eb71e2eaf13bbf998f9edf99a14c35) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif
        Py_DECREF(cache_frame_c5eb71e2eaf13bbf998f9edf99a14c35);
        cache_frame_c5eb71e2eaf13bbf998f9edf99a14c35 = NULL;
    }

    assertFrameObject(frame_c5eb71e2eaf13bbf998f9edf99a14c35);

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto function_exception_exit;
    frame_no_exception_1:;
    tmp_return_value = Py_None;
    Py_INCREF(tmp_return_value);
    goto function_return_exit;

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:

    assert(exception_type);
    RESTORE_ERROR_OCCURRED(exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.


   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !ERROR_OCCURRED());
   return tmp_return_value;
}


static PyObject *impl_pygame$fastevent$$$function__6_wait(struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    struct Nuitka_FrameObject *frame_099b0c94f22094734376b6ea5e744ec7;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    NUITKA_MAY_BE_UNUSED nuitka_void tmp_unused;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    PyObject *tmp_return_value = NULL;
    static struct Nuitka_FrameObject *cache_frame_099b0c94f22094734376b6ea5e744ec7 = NULL;

    // Actual function body.
    if (isFrameUnusable(cache_frame_099b0c94f22094734376b6ea5e744ec7)) {
        Py_XDECREF(cache_frame_099b0c94f22094734376b6ea5e744ec7);

#if _DEBUG_REFCOUNTS
        if (cache_frame_099b0c94f22094734376b6ea5e744ec7 == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_099b0c94f22094734376b6ea5e744ec7 = MAKE_FUNCTION_FRAME(codeobj_099b0c94f22094734376b6ea5e744ec7, module_pygame$fastevent, 0);
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }

    assert(cache_frame_099b0c94f22094734376b6ea5e744ec7->m_type_description == NULL);
    frame_099b0c94f22094734376b6ea5e744ec7 = cache_frame_099b0c94f22094734376b6ea5e744ec7;

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStackCompiledFrame(frame_099b0c94f22094734376b6ea5e744ec7);
    assert(Py_REFCNT(frame_099b0c94f22094734376b6ea5e744ec7) == 2);

    // Framed code:
    {
        PyObject *tmp_called_value_1;
        PyObject *tmp_call_result_1;
        tmp_called_value_1 = GET_STRING_DICT_VALUE(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[13]);

        if (unlikely(tmp_called_value_1 == NULL)) {
            tmp_called_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[13]);
        }

        if (tmp_called_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 63;

            goto frame_exception_exit_1;
        }
        frame_099b0c94f22094734376b6ea5e744ec7->m_frame.f_lineno = 63;
        tmp_call_result_1 = CALL_FUNCTION_NO_ARGS(tmp_called_value_1);
        if (tmp_call_result_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 63;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_1);
    }
    {
        PyObject *tmp_called_instance_1;
        PyObject *tmp_expression_value_1;
        tmp_expression_value_1 = GET_STRING_DICT_VALUE(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_1 == NULL)) {
            tmp_expression_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 64;

            goto frame_exception_exit_1;
        }
        tmp_called_instance_1 = LOOKUP_ATTRIBUTE(tmp_expression_value_1, mod_consts[14]);
        if (tmp_called_instance_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 64;

            goto frame_exception_exit_1;
        }
        frame_099b0c94f22094734376b6ea5e744ec7->m_frame.f_lineno = 64;
        tmp_return_value = CALL_METHOD_NO_ARGS(tmp_called_instance_1, mod_consts[17]);
        Py_DECREF(tmp_called_instance_1);
        if (tmp_return_value == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 64;

            goto frame_exception_exit_1;
        }
        goto frame_return_exit_1;
    }


    // Put the previous frame back on top.
    popFrameStack();

    goto frame_no_exception_1;
    frame_return_exit_1:

    // Put the previous frame back on top.
    popFrameStack();

    goto function_return_exit;
    frame_exception_exit_1:


    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_099b0c94f22094734376b6ea5e744ec7, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_099b0c94f22094734376b6ea5e744ec7->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_099b0c94f22094734376b6ea5e744ec7, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_099b0c94f22094734376b6ea5e744ec7,
        type_description_1
    );


    // Release cached frame if used for exception.
    if (frame_099b0c94f22094734376b6ea5e744ec7 == cache_frame_099b0c94f22094734376b6ea5e744ec7) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif
        Py_DECREF(cache_frame_099b0c94f22094734376b6ea5e744ec7);
        cache_frame_099b0c94f22094734376b6ea5e744ec7 = NULL;
    }

    assertFrameObject(frame_099b0c94f22094734376b6ea5e744ec7);

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto function_exception_exit;
    frame_no_exception_1:;

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:

    assert(exception_type);
    RESTORE_ERROR_OCCURRED(exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.


   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !ERROR_OCCURRED());
   return tmp_return_value;
}


static PyObject *impl_pygame$fastevent$$$function__7_poll(struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    struct Nuitka_FrameObject *frame_a06781bb6092cb23dff445b4e77c8f52;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    NUITKA_MAY_BE_UNUSED nuitka_void tmp_unused;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    PyObject *tmp_return_value = NULL;
    static struct Nuitka_FrameObject *cache_frame_a06781bb6092cb23dff445b4e77c8f52 = NULL;

    // Actual function body.
    if (isFrameUnusable(cache_frame_a06781bb6092cb23dff445b4e77c8f52)) {
        Py_XDECREF(cache_frame_a06781bb6092cb23dff445b4e77c8f52);

#if _DEBUG_REFCOUNTS
        if (cache_frame_a06781bb6092cb23dff445b4e77c8f52 == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_a06781bb6092cb23dff445b4e77c8f52 = MAKE_FUNCTION_FRAME(codeobj_a06781bb6092cb23dff445b4e77c8f52, module_pygame$fastevent, 0);
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }

    assert(cache_frame_a06781bb6092cb23dff445b4e77c8f52->m_type_description == NULL);
    frame_a06781bb6092cb23dff445b4e77c8f52 = cache_frame_a06781bb6092cb23dff445b4e77c8f52;

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStackCompiledFrame(frame_a06781bb6092cb23dff445b4e77c8f52);
    assert(Py_REFCNT(frame_a06781bb6092cb23dff445b4e77c8f52) == 2);

    // Framed code:
    {
        PyObject *tmp_called_value_1;
        PyObject *tmp_call_result_1;
        tmp_called_value_1 = GET_STRING_DICT_VALUE(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[13]);

        if (unlikely(tmp_called_value_1 == NULL)) {
            tmp_called_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[13]);
        }

        if (tmp_called_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 71;

            goto frame_exception_exit_1;
        }
        frame_a06781bb6092cb23dff445b4e77c8f52->m_frame.f_lineno = 71;
        tmp_call_result_1 = CALL_FUNCTION_NO_ARGS(tmp_called_value_1);
        if (tmp_call_result_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 71;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_1);
    }
    {
        PyObject *tmp_called_instance_1;
        PyObject *tmp_expression_value_1;
        tmp_expression_value_1 = GET_STRING_DICT_VALUE(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_1 == NULL)) {
            tmp_expression_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 72;

            goto frame_exception_exit_1;
        }
        tmp_called_instance_1 = LOOKUP_ATTRIBUTE(tmp_expression_value_1, mod_consts[14]);
        if (tmp_called_instance_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 72;

            goto frame_exception_exit_1;
        }
        frame_a06781bb6092cb23dff445b4e77c8f52->m_frame.f_lineno = 72;
        tmp_return_value = CALL_METHOD_NO_ARGS(tmp_called_instance_1, mod_consts[19]);
        Py_DECREF(tmp_called_instance_1);
        if (tmp_return_value == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 72;

            goto frame_exception_exit_1;
        }
        goto frame_return_exit_1;
    }


    // Put the previous frame back on top.
    popFrameStack();

    goto frame_no_exception_1;
    frame_return_exit_1:

    // Put the previous frame back on top.
    popFrameStack();

    goto function_return_exit;
    frame_exception_exit_1:


    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_a06781bb6092cb23dff445b4e77c8f52, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_a06781bb6092cb23dff445b4e77c8f52->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_a06781bb6092cb23dff445b4e77c8f52, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_a06781bb6092cb23dff445b4e77c8f52,
        type_description_1
    );


    // Release cached frame if used for exception.
    if (frame_a06781bb6092cb23dff445b4e77c8f52 == cache_frame_a06781bb6092cb23dff445b4e77c8f52) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif
        Py_DECREF(cache_frame_a06781bb6092cb23dff445b4e77c8f52);
        cache_frame_a06781bb6092cb23dff445b4e77c8f52 = NULL;
    }

    assertFrameObject(frame_a06781bb6092cb23dff445b4e77c8f52);

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto function_exception_exit;
    frame_no_exception_1:;

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:

    assert(exception_type);
    RESTORE_ERROR_OCCURRED(exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.


   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !ERROR_OCCURRED());
   return tmp_return_value;
}


static PyObject *impl_pygame$fastevent$$$function__8_get(struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    struct Nuitka_FrameObject *frame_683e7017b199f468680c80589e615920;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    NUITKA_MAY_BE_UNUSED nuitka_void tmp_unused;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    PyObject *tmp_return_value = NULL;
    static struct Nuitka_FrameObject *cache_frame_683e7017b199f468680c80589e615920 = NULL;

    // Actual function body.
    if (isFrameUnusable(cache_frame_683e7017b199f468680c80589e615920)) {
        Py_XDECREF(cache_frame_683e7017b199f468680c80589e615920);

#if _DEBUG_REFCOUNTS
        if (cache_frame_683e7017b199f468680c80589e615920 == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_683e7017b199f468680c80589e615920 = MAKE_FUNCTION_FRAME(codeobj_683e7017b199f468680c80589e615920, module_pygame$fastevent, 0);
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }

    assert(cache_frame_683e7017b199f468680c80589e615920->m_type_description == NULL);
    frame_683e7017b199f468680c80589e615920 = cache_frame_683e7017b199f468680c80589e615920;

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStackCompiledFrame(frame_683e7017b199f468680c80589e615920);
    assert(Py_REFCNT(frame_683e7017b199f468680c80589e615920) == 2);

    // Framed code:
    {
        PyObject *tmp_called_value_1;
        PyObject *tmp_call_result_1;
        tmp_called_value_1 = GET_STRING_DICT_VALUE(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[13]);

        if (unlikely(tmp_called_value_1 == NULL)) {
            tmp_called_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[13]);
        }

        if (tmp_called_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 79;

            goto frame_exception_exit_1;
        }
        frame_683e7017b199f468680c80589e615920->m_frame.f_lineno = 79;
        tmp_call_result_1 = CALL_FUNCTION_NO_ARGS(tmp_called_value_1);
        if (tmp_call_result_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 79;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_1);
    }
    {
        PyObject *tmp_called_value_2;
        PyObject *tmp_expression_value_1;
        PyObject *tmp_expression_value_2;
        tmp_expression_value_2 = GET_STRING_DICT_VALUE(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_2 == NULL)) {
            tmp_expression_value_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 80;

            goto frame_exception_exit_1;
        }
        tmp_expression_value_1 = LOOKUP_ATTRIBUTE(tmp_expression_value_2, mod_consts[14]);
        if (tmp_expression_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 80;

            goto frame_exception_exit_1;
        }
        tmp_called_value_2 = LOOKUP_ATTRIBUTE(tmp_expression_value_1, mod_consts[21]);
        Py_DECREF(tmp_expression_value_1);
        if (tmp_called_value_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 80;

            goto frame_exception_exit_1;
        }
        frame_683e7017b199f468680c80589e615920->m_frame.f_lineno = 80;
        tmp_return_value = CALL_FUNCTION_NO_ARGS(tmp_called_value_2);
        Py_DECREF(tmp_called_value_2);
        if (tmp_return_value == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 80;

            goto frame_exception_exit_1;
        }
        goto frame_return_exit_1;
    }


    // Put the previous frame back on top.
    popFrameStack();

    goto frame_no_exception_1;
    frame_return_exit_1:

    // Put the previous frame back on top.
    popFrameStack();

    goto function_return_exit;
    frame_exception_exit_1:


    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_683e7017b199f468680c80589e615920, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_683e7017b199f468680c80589e615920->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_683e7017b199f468680c80589e615920, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_683e7017b199f468680c80589e615920,
        type_description_1
    );


    // Release cached frame if used for exception.
    if (frame_683e7017b199f468680c80589e615920 == cache_frame_683e7017b199f468680c80589e615920) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif
        Py_DECREF(cache_frame_683e7017b199f468680c80589e615920);
        cache_frame_683e7017b199f468680c80589e615920 = NULL;
    }

    assertFrameObject(frame_683e7017b199f468680c80589e615920);

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto function_exception_exit;
    frame_no_exception_1:;

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:

    assert(exception_type);
    RESTORE_ERROR_OCCURRED(exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.


   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !ERROR_OCCURRED());
   return tmp_return_value;
}


static PyObject *impl_pygame$fastevent$$$function__9_post(struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_event = python_pars[0];
    struct Nuitka_FrameObject *frame_53618d9d517a863327a483b66b1ee760;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    NUITKA_MAY_BE_UNUSED nuitka_void tmp_unused;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    static struct Nuitka_FrameObject *cache_frame_53618d9d517a863327a483b66b1ee760 = NULL;
    PyObject *tmp_return_value = NULL;

    // Actual function body.
    if (isFrameUnusable(cache_frame_53618d9d517a863327a483b66b1ee760)) {
        Py_XDECREF(cache_frame_53618d9d517a863327a483b66b1ee760);

#if _DEBUG_REFCOUNTS
        if (cache_frame_53618d9d517a863327a483b66b1ee760 == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_53618d9d517a863327a483b66b1ee760 = MAKE_FUNCTION_FRAME(codeobj_53618d9d517a863327a483b66b1ee760, module_pygame$fastevent, sizeof(void *));
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }

    assert(cache_frame_53618d9d517a863327a483b66b1ee760->m_type_description == NULL);
    frame_53618d9d517a863327a483b66b1ee760 = cache_frame_53618d9d517a863327a483b66b1ee760;

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStackCompiledFrame(frame_53618d9d517a863327a483b66b1ee760);
    assert(Py_REFCNT(frame_53618d9d517a863327a483b66b1ee760) == 2);

    // Framed code:
    {
        PyObject *tmp_called_value_1;
        PyObject *tmp_call_result_1;
        tmp_called_value_1 = GET_STRING_DICT_VALUE(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[13]);

        if (unlikely(tmp_called_value_1 == NULL)) {
            tmp_called_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[13]);
        }

        if (tmp_called_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 87;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        frame_53618d9d517a863327a483b66b1ee760->m_frame.f_lineno = 87;
        tmp_call_result_1 = CALL_FUNCTION_NO_ARGS(tmp_called_value_1);
        if (tmp_call_result_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 87;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_1);
    }
    {
        PyObject *tmp_called_instance_1;
        PyObject *tmp_expression_value_1;
        PyObject *tmp_call_result_2;
        PyObject *tmp_args_element_value_1;
        tmp_expression_value_1 = GET_STRING_DICT_VALUE(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_1 == NULL)) {
            tmp_expression_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 88;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        tmp_called_instance_1 = LOOKUP_ATTRIBUTE(tmp_expression_value_1, mod_consts[14]);
        if (tmp_called_instance_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 88;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_event);
        tmp_args_element_value_1 = par_event;
        frame_53618d9d517a863327a483b66b1ee760->m_frame.f_lineno = 88;
        tmp_call_result_2 = CALL_METHOD_WITH_SINGLE_ARG(tmp_called_instance_1, mod_consts[23], tmp_args_element_value_1);
        Py_DECREF(tmp_called_instance_1);
        if (tmp_call_result_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 88;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_2);
    }


    // Put the previous frame back on top.
    popFrameStack();

    goto frame_no_exception_1;
    frame_exception_exit_1:


    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_53618d9d517a863327a483b66b1ee760, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_53618d9d517a863327a483b66b1ee760->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_53618d9d517a863327a483b66b1ee760, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_53618d9d517a863327a483b66b1ee760,
        type_description_1,
        par_event
    );


    // Release cached frame if used for exception.
    if (frame_53618d9d517a863327a483b66b1ee760 == cache_frame_53618d9d517a863327a483b66b1ee760) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif
        Py_DECREF(cache_frame_53618d9d517a863327a483b66b1ee760);
        cache_frame_53618d9d517a863327a483b66b1ee760 = NULL;
    }

    assertFrameObject(frame_53618d9d517a863327a483b66b1ee760);

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto function_exception_exit;
    frame_no_exception_1:;
    tmp_return_value = Py_None;
    Py_INCREF(tmp_return_value);
    goto function_return_exit;

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:
    CHECK_OBJECT(par_event);
    Py_DECREF(par_event);
    assert(exception_type);
    RESTORE_ERROR_OCCURRED(exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_event);
    Py_DECREF(par_event);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !ERROR_OCCURRED());
   return tmp_return_value;
}



static PyObject *MAKE_FUNCTION_pygame$fastevent$$$function__1__ft_init_check() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_pygame$fastevent$$$function__1__ft_init_check,
        mod_consts[13],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_c46da681bb4a310523970e77d37f20d5,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_pygame$fastevent,
        mod_consts[3],
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_pygame$fastevent$$$function__2__quit_hook() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_pygame$fastevent$$$function__2__quit_hook,
        mod_consts[10],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_98250ffa89a8b9574d0d88a4ace068bd,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_pygame$fastevent,
        mod_consts[4],
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_pygame$fastevent$$$function__3_init() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_pygame$fastevent$$$function__3_init,
        mod_consts[39],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_f691136a0b5ae56578dda9ab384c943d,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_pygame$fastevent,
        mod_consts[11],
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_pygame$fastevent$$$function__4_get_init() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_pygame$fastevent$$$function__4_get_init,
        mod_consts[7],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_7d8282e62902e59592aec14bf40e9db8,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_pygame$fastevent,
        mod_consts[12],
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_pygame$fastevent$$$function__5_pump() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_pygame$fastevent$$$function__5_pump,
        mod_consts[15],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_c5eb71e2eaf13bbf998f9edf99a14c35,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_pygame$fastevent,
        mod_consts[16],
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_pygame$fastevent$$$function__6_wait() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_pygame$fastevent$$$function__6_wait,
        mod_consts[17],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_099b0c94f22094734376b6ea5e744ec7,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_pygame$fastevent,
        mod_consts[18],
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_pygame$fastevent$$$function__7_poll() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_pygame$fastevent$$$function__7_poll,
        mod_consts[19],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_a06781bb6092cb23dff445b4e77c8f52,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_pygame$fastevent,
        mod_consts[20],
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_pygame$fastevent$$$function__8_get() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_pygame$fastevent$$$function__8_get,
        mod_consts[21],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_683e7017b199f468680c80589e615920,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_pygame$fastevent,
        mod_consts[22],
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_pygame$fastevent$$$function__9_post(PyObject *annotations) {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_pygame$fastevent$$$function__9_post,
        mod_consts[23],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_53618d9d517a863327a483b66b1ee760,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        annotations,
#endif
        module_pygame$fastevent,
        mod_consts[24],
        NULL,
        0
    );


    return (PyObject *)result;
}


extern void _initCompiledCellType();
extern void _initCompiledGeneratorType();
extern void _initCompiledFunctionType();
extern void _initCompiledMethodType();
extern void _initCompiledFrameType();

extern PyTypeObject Nuitka_Loader_Type;

#ifdef _NUITKA_PLUGIN_DILL_ENABLED
// Provide a way to create find a function via its C code and create it back
// in another process, useful for multiprocessing extensions like dill
extern void registerDillPluginTables(char const *module_name, PyMethodDef *reduce_compiled_function, PyMethodDef *create_compiled_function);

function_impl_code functable_pygame$fastevent[] = {
    impl_pygame$fastevent$$$function__1__ft_init_check,
    impl_pygame$fastevent$$$function__2__quit_hook,
    impl_pygame$fastevent$$$function__3_init,
    impl_pygame$fastevent$$$function__4_get_init,
    impl_pygame$fastevent$$$function__5_pump,
    impl_pygame$fastevent$$$function__6_wait,
    impl_pygame$fastevent$$$function__7_poll,
    impl_pygame$fastevent$$$function__8_get,
    impl_pygame$fastevent$$$function__9_post,
    NULL
};

static char const *_reduce_compiled_function_argnames[] = {
    "func",
    NULL
};

static PyObject *_reduce_compiled_function(PyObject *self, PyObject *args, PyObject *kwds) {
    PyObject *func;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O:reduce_compiled_function", (char **)_reduce_compiled_function_argnames, &func, NULL)) {
        return NULL;
    }

    if (Nuitka_Function_Check(func) == false) {
        SET_CURRENT_EXCEPTION_TYPE0_STR(PyExc_TypeError, "not a compiled function");
        return NULL;
    }

    struct Nuitka_FunctionObject *function = (struct Nuitka_FunctionObject *)func;

    function_impl_code *current = functable_pygame$fastevent;
    int offset = 0;

    while (*current != NULL) {
        if (*current == function->m_c_code) {
            break;
        }

        current += 1;
        offset += 1;
    }

    if (*current == NULL) {
        SET_CURRENT_EXCEPTION_TYPE0_STR(PyExc_TypeError, "Cannot find compiled function in module.");
        return NULL;
    }

    PyObject *code_object_desc = MAKE_TUPLE_EMPTY(6);
    PyTuple_SET_ITEM0(code_object_desc, 0, function->m_code_object->co_filename);
    PyTuple_SET_ITEM0(code_object_desc, 1, function->m_code_object->co_name);
    PyTuple_SET_ITEM(code_object_desc, 2, PyLong_FromLong(function->m_code_object->co_firstlineno));
    PyTuple_SET_ITEM0(code_object_desc, 3, function->m_code_object->co_varnames);
    PyTuple_SET_ITEM(code_object_desc, 4, PyLong_FromLong(function->m_code_object->co_argcount));
    PyTuple_SET_ITEM(code_object_desc, 5, PyLong_FromLong(function->m_code_object->co_flags));

    CHECK_OBJECT_DEEP(code_object_desc);

    PyObject *result = MAKE_TUPLE_EMPTY(4);
    PyTuple_SET_ITEM(result, 0, PyLong_FromLong(offset));
    PyTuple_SET_ITEM(result, 1, code_object_desc);
    PyTuple_SET_ITEM0(result, 2, function->m_defaults);
    PyTuple_SET_ITEM0(result, 3, function->m_doc != NULL ? function->m_doc : Py_None);

    CHECK_OBJECT_DEEP(result);

    return result;
}

static PyMethodDef _method_def_reduce_compiled_function = {"reduce_compiled_function", (PyCFunction)_reduce_compiled_function,
                                                           METH_VARARGS | METH_KEYWORDS, NULL};

static char const *_create_compiled_function_argnames[] = {
    "func",
    "code_object_desc",
    "defaults",
    "doc",
    NULL
};


static PyObject *_create_compiled_function(PyObject *self, PyObject *args, PyObject *kwds) {
    CHECK_OBJECT_DEEP(args);

    PyObject *func;
    PyObject *code_object_desc;
    PyObject *defaults;
    PyObject *doc;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "OOOO:create_compiled_function", (char **)_create_compiled_function_argnames, &func, &code_object_desc, &defaults, &doc, NULL)) {
        return NULL;
    }

    int offset = PyLong_AsLong(func);

    if (offset == -1 && ERROR_OCCURRED()) {
        return NULL;
    }

    if (offset > sizeof(functable_pygame$fastevent) || offset < 0) {
        SET_CURRENT_EXCEPTION_TYPE0_STR(PyExc_TypeError, "Wrong offset for compiled function.");
        return NULL;
    }

    PyObject *filename = PyTuple_GET_ITEM(code_object_desc, 0);
    PyObject *function_name = PyTuple_GET_ITEM(code_object_desc, 1);
    PyObject *line = PyTuple_GET_ITEM(code_object_desc, 2);
    int line_int = PyLong_AsLong(line);
    assert(!ERROR_OCCURRED());

    PyObject *argnames = PyTuple_GET_ITEM(code_object_desc, 3);
    PyObject *arg_count = PyTuple_GET_ITEM(code_object_desc, 4);
    int arg_count_int = PyLong_AsLong(arg_count);
    assert(!ERROR_OCCURRED());
    PyObject *flags = PyTuple_GET_ITEM(code_object_desc, 5);
    int flags_int = PyLong_AsLong(flags);
    assert(!ERROR_OCCURRED());

    PyCodeObject *code_object = MAKE_CODE_OBJECT(
        filename,
        line_int,
        flags_int,
        function_name,
        function_name, // TODO: function_qualname
        argnames,
        NULL, // freevars
        arg_count_int,
        0, // TODO: Missing kw_only_count
        0 // TODO: Missing pos_only_count
    );

    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        functable_pygame$fastevent[offset],
        code_object->co_name,
#if PYTHON_VERSION >= 0x300
        NULL, // TODO: Not transferring qualname yet
#endif
        code_object,
        defaults,
#if PYTHON_VERSION >= 0x300
        NULL, // kwdefaults are done on the outside currently
        NULL, // TODO: Not transferring annotations
#endif
        module_pygame$fastevent,
        doc,
        NULL,
        0
    );

    return (PyObject *)result;
}

static PyMethodDef _method_def_create_compiled_function = {
    "create_compiled_function",
    (PyCFunction)_create_compiled_function,
    METH_VARARGS | METH_KEYWORDS, NULL
};


#endif

// Internal entry point for module code.
PyObject *modulecode_pygame$fastevent(PyObject *module, struct Nuitka_MetaPathBasedLoaderEntry const *loader_entry) {
    // Report entry to PGO.
    PGO_onModuleEntered("pygame.fastevent");

    // Store the module for future use.
    module_pygame$fastevent = module;

    // Modules can be loaded again in case of errors, avoid the init being done again.
    static bool init_done = false;

    if (init_done == false) {
#if defined(_NUITKA_MODULE) && 0
        // In case of an extension module loaded into a process, we need to call
        // initialization here because that's the first and potentially only time
        // we are going called.

        // Initialize the constant values used.
        _initBuiltinModule();
        createGlobalConstants();

        /* Initialize the compiled types of Nuitka. */
        _initCompiledCellType();
        _initCompiledGeneratorType();
        _initCompiledFunctionType();
        _initCompiledMethodType();
        _initCompiledFrameType();

        _initSlotCompare();
#if PYTHON_VERSION >= 0x270
        _initSlotIterNext();
#endif

        patchTypeComparison();

        // Enable meta path based loader if not already done.
#ifdef _NUITKA_TRACE
        PRINT_STRING("pygame.fastevent: Calling setupMetaPathBasedLoader().\n");
#endif
        setupMetaPathBasedLoader();

#if PYTHON_VERSION >= 0x300
        patchInspectModule();
#endif

#endif

        /* The constants only used by this module are created now. */
        NUITKA_PRINT_TRACE("pygame.fastevent: Calling createModuleConstants().\n");
        createModuleConstants();

        createModuleCodeObjects();

        init_done = true;
    }

    // PRINT_STRING("in initpygame$fastevent\n");

    moduledict_pygame$fastevent = MODULE_DICT(module_pygame$fastevent);

#ifdef _NUITKA_PLUGIN_DILL_ENABLED
    registerDillPluginTables(loader_entry->name, &_method_def_reduce_compiled_function, &_method_def_create_compiled_function);
#endif

    // Set "__compiled__" to what version information we have.
    UPDATE_STRING_DICT0(
        moduledict_pygame$fastevent,
        (Nuitka_StringObject *)const_str_plain___compiled__,
        Nuitka_dunder_compiled_value
    );

    // Update "__package__" value to what it ought to be.
    {
#if 0
        UPDATE_STRING_DICT0(
            moduledict_pygame$fastevent,
            (Nuitka_StringObject *)const_str_plain___package__,
            mod_consts[42]
        );
#elif 0
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_pygame$fastevent, (Nuitka_StringObject *)const_str_plain___name__);

        UPDATE_STRING_DICT0(
            moduledict_pygame$fastevent,
            (Nuitka_StringObject *)const_str_plain___package__,
            module_name
        );
#else

#if PYTHON_VERSION < 0x300
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_pygame$fastevent, (Nuitka_StringObject *)const_str_plain___name__);
        char const *module_name_cstr = PyString_AS_STRING(module_name);

        char const *last_dot = strrchr(module_name_cstr, '.');

        if (last_dot != NULL) {
            UPDATE_STRING_DICT1(
                moduledict_pygame$fastevent,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyString_FromStringAndSize(module_name_cstr, last_dot - module_name_cstr)
            );
        }
#else
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_pygame$fastevent, (Nuitka_StringObject *)const_str_plain___name__);
        Py_ssize_t dot_index = PyUnicode_Find(module_name, const_str_dot, 0, PyUnicode_GetLength(module_name), -1);

        if (dot_index != -1) {
            UPDATE_STRING_DICT1(
                moduledict_pygame$fastevent,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyUnicode_Substring(module_name, 0, dot_index)
            );
        }
#endif
#endif
    }

    CHECK_OBJECT(module_pygame$fastevent);

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    if (GET_STRING_DICT_VALUE(moduledict_pygame$fastevent, (Nuitka_StringObject *)const_str_plain___builtins__) == NULL) {
        PyObject *value = (PyObject *)builtin_module;

        // Check if main module, not a dict then but the module itself.
#if defined(_NUITKA_MODULE) || !0
        value = PyModule_GetDict(value);
#endif

        UPDATE_STRING_DICT0(moduledict_pygame$fastevent, (Nuitka_StringObject *)const_str_plain___builtins__, value);
    }

    UPDATE_STRING_DICT0(moduledict_pygame$fastevent, (Nuitka_StringObject *)const_str_plain___loader__, (PyObject *)&Nuitka_Loader_Type);

#if PYTHON_VERSION >= 0x340
// Set the "__spec__" value

#if 0
    // Main modules just get "None" as spec.
    UPDATE_STRING_DICT0(moduledict_pygame$fastevent, (Nuitka_StringObject *)const_str_plain___spec__, Py_None);
#else
    // Other modules get a "ModuleSpec" from the standard mechanism.
    {
        PyObject *bootstrap_module = getImportLibBootstrapModule();
        CHECK_OBJECT(bootstrap_module);

        PyObject *_spec_from_module = PyObject_GetAttrString(bootstrap_module, "_spec_from_module");
        CHECK_OBJECT(_spec_from_module);

        PyObject *spec_value = CALL_FUNCTION_WITH_SINGLE_ARG(_spec_from_module, module_pygame$fastevent);
        Py_DECREF(_spec_from_module);

        // We can assume this to never fail, or else we are in trouble anyway.
        // CHECK_OBJECT(spec_value);

        if (spec_value == NULL) {
            PyErr_PrintEx(0);
            abort();
        }

// Mark the execution in the "__spec__" value.
        SET_ATTRIBUTE(spec_value, const_str_plain__initializing, Py_True);

        UPDATE_STRING_DICT1(moduledict_pygame$fastevent, (Nuitka_StringObject *)const_str_plain___spec__, spec_value);
    }
#endif
#endif

    // Temp variables if any
    PyObject *tmp_import_from_1__module = NULL;
    struct Nuitka_FrameObject *frame_a44e3400414d04942b82894fd318c250;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    bool tmp_result;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    int tmp_res;

    // Module code.
    {
        PyObject *tmp_assign_source_1;
        tmp_assign_source_1 = mod_consts[25];
        UPDATE_STRING_DICT0(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[26], tmp_assign_source_1);
    }
    {
        PyObject *tmp_assign_source_2;
        tmp_assign_source_2 = mod_consts[27];
        UPDATE_STRING_DICT0(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[28], tmp_assign_source_2);
    }
    frame_a44e3400414d04942b82894fd318c250 = MAKE_MODULE_FRAME(codeobj_a44e3400414d04942b82894fd318c250, module_pygame$fastevent);

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStackCompiledFrame(frame_a44e3400414d04942b82894fd318c250);
    assert(Py_REFCNT(frame_a44e3400414d04942b82894fd318c250) == 2);

    // Framed code:
    {
        PyObject *tmp_assattr_value_1;
        PyObject *tmp_assattr_target_1;
        tmp_assattr_value_1 = mod_consts[27];
        tmp_assattr_target_1 = GET_STRING_DICT_VALUE(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[29]);

        if (unlikely(tmp_assattr_target_1 == NULL)) {
            tmp_assattr_target_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[29]);
        }

        assert(!(tmp_assattr_target_1 == NULL));
        tmp_result = SET_ATTRIBUTE(tmp_assattr_target_1, mod_consts[30], tmp_assattr_value_1);
        if (tmp_result == false) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_assattr_value_2;
        PyObject *tmp_assattr_target_2;
        tmp_assattr_value_2 = Py_True;
        tmp_assattr_target_2 = GET_STRING_DICT_VALUE(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[29]);

        if (unlikely(tmp_assattr_target_2 == NULL)) {
            tmp_assattr_target_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[29]);
        }

        assert(!(tmp_assattr_target_2 == NULL));
        tmp_result = SET_ATTRIBUTE(tmp_assattr_target_2, mod_consts[31], tmp_assattr_value_2);
        if (tmp_result == false) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_assign_source_3;
        tmp_assign_source_3 = Py_None;
        UPDATE_STRING_DICT0(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[32], tmp_assign_source_3);
    }
    {
        PyObject *tmp_assign_source_4;
        PyObject *tmp_name_value_1;
        PyObject *tmp_globals_arg_value_1;
        PyObject *tmp_locals_arg_value_1;
        PyObject *tmp_fromlist_value_1;
        PyObject *tmp_level_value_1;
        tmp_name_value_1 = mod_consts[33];
        tmp_globals_arg_value_1 = (PyObject *)moduledict_pygame$fastevent;
        tmp_locals_arg_value_1 = Py_None;
        tmp_fromlist_value_1 = Py_None;
        tmp_level_value_1 = mod_consts[34];
        frame_a44e3400414d04942b82894fd318c250->m_frame.f_lineno = 8;
        tmp_assign_source_4 = IMPORT_MODULE5(tmp_name_value_1, tmp_globals_arg_value_1, tmp_locals_arg_value_1, tmp_fromlist_value_1, tmp_level_value_1);
        if (tmp_assign_source_4 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 8;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[5], tmp_assign_source_4);
    }
    {
        PyObject *tmp_assign_source_5;
        PyObject *tmp_name_value_2;
        PyObject *tmp_globals_arg_value_2;
        PyObject *tmp_locals_arg_value_2;
        PyObject *tmp_fromlist_value_2;
        PyObject *tmp_level_value_2;
        tmp_name_value_2 = mod_consts[35];
        tmp_globals_arg_value_2 = (PyObject *)moduledict_pygame$fastevent;
        tmp_locals_arg_value_2 = Py_None;
        tmp_fromlist_value_2 = Py_None;
        tmp_level_value_2 = mod_consts[34];
        frame_a44e3400414d04942b82894fd318c250->m_frame.f_lineno = 9;
        tmp_assign_source_5 = IMPORT_MODULE5(tmp_name_value_2, tmp_globals_arg_value_2, tmp_locals_arg_value_2, tmp_fromlist_value_2, tmp_level_value_2);
        if (tmp_assign_source_5 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 9;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[5], tmp_assign_source_5);
    }
    {
        PyObject *tmp_assign_source_6;
        PyObject *tmp_name_value_3;
        PyObject *tmp_globals_arg_value_3;
        PyObject *tmp_locals_arg_value_3;
        PyObject *tmp_fromlist_value_3;
        PyObject *tmp_level_value_3;
        tmp_name_value_3 = mod_consts[5];
        tmp_globals_arg_value_3 = (PyObject *)moduledict_pygame$fastevent;
        tmp_locals_arg_value_3 = Py_None;
        tmp_fromlist_value_3 = mod_consts[36];
        tmp_level_value_3 = mod_consts[34];
        frame_a44e3400414d04942b82894fd318c250->m_frame.f_lineno = 10;
        tmp_assign_source_6 = IMPORT_MODULE5(tmp_name_value_3, tmp_globals_arg_value_3, tmp_locals_arg_value_3, tmp_fromlist_value_3, tmp_level_value_3);
        if (tmp_assign_source_6 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 10;

            goto frame_exception_exit_1;
        }
        assert(tmp_import_from_1__module == NULL);
        tmp_import_from_1__module = tmp_assign_source_6;
    }
    // Tried code:
    {
        PyObject *tmp_assign_source_7;
        PyObject *tmp_import_name_from_1;
        CHECK_OBJECT(tmp_import_from_1__module);
        tmp_import_name_from_1 = tmp_import_from_1__module;
        if (PyModule_Check(tmp_import_name_from_1)) {
            tmp_assign_source_7 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_1,
                (PyObject *)moduledict_pygame$fastevent,
                mod_consts[1],
                mod_consts[34]
            );
        } else {
            tmp_assign_source_7 = IMPORT_NAME_FROM_MODULE(tmp_import_name_from_1, mod_consts[1]);
        }

        if (tmp_assign_source_7 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 10;

            goto try_except_handler_1;
        }
        UPDATE_STRING_DICT1(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[1], tmp_assign_source_7);
    }
    {
        PyObject *tmp_assign_source_8;
        PyObject *tmp_import_name_from_2;
        CHECK_OBJECT(tmp_import_from_1__module);
        tmp_import_name_from_2 = tmp_import_from_1__module;
        if (PyModule_Check(tmp_import_name_from_2)) {
            tmp_assign_source_8 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_2,
                (PyObject *)moduledict_pygame$fastevent,
                mod_consts[9],
                mod_consts[34]
            );
        } else {
            tmp_assign_source_8 = IMPORT_NAME_FROM_MODULE(tmp_import_name_from_2, mod_consts[9]);
        }

        if (tmp_assign_source_8 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 10;

            goto try_except_handler_1;
        }
        UPDATE_STRING_DICT1(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[9], tmp_assign_source_8);
    }
    goto try_end_1;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    CHECK_OBJECT(tmp_import_from_1__module);
    Py_DECREF(tmp_import_from_1__module);
    tmp_import_from_1__module = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto frame_exception_exit_1;
    // End of try:
    try_end_1:;
    CHECK_OBJECT(tmp_import_from_1__module);
    Py_DECREF(tmp_import_from_1__module);
    tmp_import_from_1__module = NULL;
    {
        PyObject *tmp_assign_source_9;
        PyObject *tmp_import_name_from_3;
        PyObject *tmp_name_value_4;
        PyObject *tmp_globals_arg_value_4;
        PyObject *tmp_locals_arg_value_4;
        PyObject *tmp_fromlist_value_4;
        PyObject *tmp_level_value_4;
        tmp_name_value_4 = mod_consts[33];
        tmp_globals_arg_value_4 = (PyObject *)moduledict_pygame$fastevent;
        tmp_locals_arg_value_4 = Py_None;
        tmp_fromlist_value_4 = mod_consts[37];
        tmp_level_value_4 = mod_consts[34];
        frame_a44e3400414d04942b82894fd318c250->m_frame.f_lineno = 11;
        tmp_import_name_from_3 = IMPORT_MODULE5(tmp_name_value_4, tmp_globals_arg_value_4, tmp_locals_arg_value_4, tmp_fromlist_value_4, tmp_level_value_4);
        if (tmp_import_name_from_3 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 11;

            goto frame_exception_exit_1;
        }
        if (PyModule_Check(tmp_import_name_from_3)) {
            tmp_assign_source_9 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_3,
                (PyObject *)moduledict_pygame$fastevent,
                mod_consts[38],
                mod_consts[34]
            );
        } else {
            tmp_assign_source_9 = IMPORT_NAME_FROM_MODULE(tmp_import_name_from_3, mod_consts[38]);
        }

        Py_DECREF(tmp_import_name_from_3);
        if (tmp_assign_source_9 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 11;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[38], tmp_assign_source_9);
    }


    // Put the previous frame back on top.
    popFrameStack();

    goto frame_no_exception_1;
    frame_exception_exit_1:


    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_a44e3400414d04942b82894fd318c250, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_a44e3400414d04942b82894fd318c250->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_a44e3400414d04942b82894fd318c250, exception_lineno);
    }



    assertFrameObject(frame_a44e3400414d04942b82894fd318c250);

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto module_exception_exit;
    frame_no_exception_1:;
    {
        PyObject *tmp_assign_source_10;
        tmp_assign_source_10 = Py_False;
        UPDATE_STRING_DICT0(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[0], tmp_assign_source_10);
    }
    {
        PyObject *tmp_assign_source_11;


        tmp_assign_source_11 = MAKE_FUNCTION_pygame$fastevent$$$function__1__ft_init_check();

        UPDATE_STRING_DICT1(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[13], tmp_assign_source_11);
    }
    {
        PyObject *tmp_assign_source_12;


        tmp_assign_source_12 = MAKE_FUNCTION_pygame$fastevent$$$function__2__quit_hook();

        UPDATE_STRING_DICT1(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[10], tmp_assign_source_12);
    }
    {
        PyObject *tmp_assign_source_13;


        tmp_assign_source_13 = MAKE_FUNCTION_pygame$fastevent$$$function__3_init();

        UPDATE_STRING_DICT1(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[39], tmp_assign_source_13);
    }
    {
        PyObject *tmp_assign_source_14;


        tmp_assign_source_14 = MAKE_FUNCTION_pygame$fastevent$$$function__4_get_init();

        UPDATE_STRING_DICT1(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[7], tmp_assign_source_14);
    }
    {
        PyObject *tmp_assign_source_15;


        tmp_assign_source_15 = MAKE_FUNCTION_pygame$fastevent$$$function__5_pump();

        UPDATE_STRING_DICT1(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[15], tmp_assign_source_15);
    }
    {
        PyObject *tmp_assign_source_16;


        tmp_assign_source_16 = MAKE_FUNCTION_pygame$fastevent$$$function__6_wait();

        UPDATE_STRING_DICT1(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[17], tmp_assign_source_16);
    }
    {
        PyObject *tmp_assign_source_17;


        tmp_assign_source_17 = MAKE_FUNCTION_pygame$fastevent$$$function__7_poll();

        UPDATE_STRING_DICT1(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[19], tmp_assign_source_17);
    }
    {
        PyObject *tmp_assign_source_18;


        tmp_assign_source_18 = MAKE_FUNCTION_pygame$fastevent$$$function__8_get();

        UPDATE_STRING_DICT1(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[21], tmp_assign_source_18);
    }
    {
        PyObject *tmp_assign_source_19;
        PyObject *tmp_annotations_1;
        PyObject *tmp_dict_key_1;
        PyObject *tmp_dict_value_1;
        tmp_dict_key_1 = mod_consts[14];
        tmp_dict_value_1 = GET_STRING_DICT_VALUE(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[38]);

        if (unlikely(tmp_dict_value_1 == NULL)) {
            tmp_dict_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[38]);
        }

        assert(!(tmp_dict_value_1 == NULL));
        tmp_annotations_1 = _PyDict_NewPresized( 1 );
        tmp_res = PyDict_SetItem(tmp_annotations_1, tmp_dict_key_1, tmp_dict_value_1);
        assert(!(tmp_res != 0));


        tmp_assign_source_19 = MAKE_FUNCTION_pygame$fastevent$$$function__9_post(tmp_annotations_1);

        UPDATE_STRING_DICT1(moduledict_pygame$fastevent, (Nuitka_StringObject *)mod_consts[23], tmp_assign_source_19);
    }

    // Report to PGO about leaving the module without error.
    PGO_onModuleExit("pygame.fastevent", false);

    Py_INCREF(module_pygame$fastevent);
    return module_pygame$fastevent;
    module_exception_exit:

#if defined(_NUITKA_MODULE) && 0
    {
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_pygame$fastevent, (Nuitka_StringObject *)const_str_plain___name__);

        if (module_name != NULL) {
            Nuitka_DelModule(module_name);
        }
    }
#endif
    PGO_onModuleExit("pygame$fastevent", false);

    RESTORE_ERROR_OCCURRED(exception_type, exception_value, exception_tb);
    return NULL;
}
