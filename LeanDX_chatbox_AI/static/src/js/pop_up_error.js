/** @odoo-module **/


import { registry } from '@web/core/registry';
const { Component, mount} = owl





export class Error1 extends  Component{
    message = '';
    type = '';
    setup(message, type) {
        super.setup();
        this.message = message;
        this.type = type;
    }



}


Error.template = "LeanDX_chatbox_AI.error";

// remember the tag name we put in the first step
registry.category("actions").add("LeanDX_chatbox_AI.error_action", Error1);




