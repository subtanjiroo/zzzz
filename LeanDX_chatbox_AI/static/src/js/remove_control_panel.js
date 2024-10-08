/** @odoo-module */



import { ControlPanel } from "@web/search/control_panel/control_panel";

import { patch } from "@web/core/utils/patch";

import { useRef, onPatched, onMounted, useState } from "@odoo/owl";



patch(ControlPanel.prototype,{

    setup() {

        super.setup();

        onMounted(() => {

            // #You can set any condition that you wish to remove the control panel at any time or from any place.

            if (this.env.searchModel && this.env.searchModel.resModel === "chatbox.ai"){

                this.root.el.style.setProperty("display", "none", "important");

            }

        });

    },

});