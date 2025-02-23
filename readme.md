## **Introduction**
The **Modify Channelbox Attributes** app provides the user with a collection of simple tools that help to speed up a rigger's workflow. 
These tools provide the ability to set, add, connect or change the state of an object's channelbox attributes. 

![tool ui](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/img/modify_cb_attrs_tool.png)

## Tool Actions
### **Reset Attributes** 
* _Reset Channels_ - For selected object(s), resets all attributes to their default values. If specific attributes are highlighted only those attributes will be reset to default. 

![reset_attributes](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/img/tool_reset_attributes.gif)

### **Match Attributes**
* _Match Transforms_ - Matches object selection's attributes to the first selection. Works for multiple object selection. 
* _Match Translate_ - Matches the translation attributes.
* _Match Rotate_ - Matches the rotation attributes.
* _Match Scale_ - Matches the scale attributes.

![match_attributes](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/img/tool_match_attributes.gif)

### **Add Attributes**
* _Add Attribute_ - Add a custom attribute. User provides name and specifies attribute type via the dropdown menu. Attribute Types defaults to 'bool'. Provide a Min/Max value if desired for float or int types. 
* _Add Separator_ - Create a channel box divider. Name provided will be converted to uppercase. If no name is provided an underscored name will (ex. __ ) be created by default. 

![add_attributes](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/img/tool_add_attributes.gif)

### **Channel Attributes**
* _Lock/Unlock Attribute_ - Works similar to the _Reset Channels_ tool. For selected object(s), lock all attributes. If attributes are already locked the opposite unlock action will be done. If specific attributes are highlighted only those attributes locked/unlocked. 

![lock_unlock_attributes](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/img/lock_unlock_attributes.gif)

* _Hide Attribute_

* _Lock + Hide Attribute_ - For selected object(s), lock and hide all attributes. Toggles unlocked and unhidden if action initialized again. If specific attributes are highlighted only those attributes affected. 

**Note**, a current bug exists where re-initializing action on specified attributes does not unlock and unhide the attributes as seen in the example gif: 

![lock_hide_attributes](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/img/lock_hide_attributes.gif)

* _Keyable/Unkeyable Attribute_ - For selected object(s), makes all attributes keyable. Toggles attributes unkeyable if action initialized again. If specific attributes are highlighted only those attributes affected. 

![keyable_unkeyable_attribute](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/img/keyable_unkeyable_attributes.gif)

* _Mute/Unmute Attribute_ - For selected object(s), mutes keyed attributes. **Note** that animation needs to be present on attributes for action to be applied. Toggles attributes unmute if action initialized again. If specific attributes are highlighted only those attributes affected. 

**Note** The _Mute_ and _Unmute_ tool have been split into separate buttons in order to get it to work.

![mute_unmute_attributes](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/img/mute_unmute_attributes.gif)

* ^ _(Reorder Attribute - Up)_
* v _(Reorder Attribute - Down)_

### **Connect Attributes**
* _Connect Attributes_ - Connects attributes of subsequent object selection to first selection. Similar to the _Reset Channels_ tool, if channelbox attributes are highlighted only those attributes will be connected.
* _Disconnect Attributes_ - Disconnects connected attributes. If attributes are highlighted then only those attributes will be disconnected. If no attributes are highlighted then all connected attributes will be disconnected.

![connect_attributes](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/img/tool_connect_attributes.gif)

