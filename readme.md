## **Introduction**
The **Modify Channelbox Attributes** app provides the user with a collection of simple tools that help to speed up the artist's workflow. 
These tools provide the ability to set, add, connect or change the state of an object's channelbox attributes. 

![tool ui](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/img/modify_cb_attrs_tool.png)

## Environment
- [x] **OS**: Windows | Linux
- [x] **Software**: Maya 2023+

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
* _Lock/Unlock Attribute_
* _Mute/Unmute Attribute_
* _Hide Attribute_
* _Unhide Last Hidden Attribute_
* _Lock + Hide Attribute_
* _Keyable/Unkeyable Attribute_
* ^ _(Reorder Attribute - Up)_
* v _(Reorder Attribute - Down)_

### **Connect Attributes**
* _Connect Attributes_ - Connects attributes of subsequent object selection to first selection. Similar to the _Reset Channels_ tool, if channelbox attributes are highlighted only those attributes will be connected.
* _Disconnect Attributes_ - Disconnects connected attributes. If attributes are highlighted then only those attributes will be disconnected. If no attributes are highlighted then all connected attributes will be disconnected.

![connect_attributes](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/img/tool_connect_attributes.gif)

