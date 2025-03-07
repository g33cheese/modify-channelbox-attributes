## **Introduction**
The **Modify Channelbox Attributes** app provides riggers with a collection of simple tools that help to speed up their workflow. 
These APP tools provide the ability to set, add, connect or change the state of an object's channelbox attributes. 

The APP is designed to speed up a rigger's workflow. Its tools reduce the number of actions (button clicks) the rigger needs to take when inputting channelbox data. It does so by removing the need for the artist to go into the channelBox's menus (Channels and Edit) or in the case of the Reset Channels action, removing the need to input data.

The APP takes these frequently used actions out of submenus and presents them front-facing to the Rigger to accurately represent how often they are accessed. The APP does this by pulling these actions out of the ChannelBox's menus with clearly represented icons that are designed for quick recognition and selection by the rigger. 


![tool ui](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/0_app/img/app_ui_screenshot.png)


## Tool Actions
### **Reset Attributes** 
* _Reset Channels_ - For selected object(s), resets all attributes to their default values. If specific attributes are highlighted only those attributes will be reset to default. 
![reset_attributes](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/0_app/img/gifs/mCBXa_reset_attributes.gif)

### **Match Attributes**
* _Match Transforms_ - Matches object selection's attributes to the first selection. Works for multiple object selection. 
![match_attributes](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/0_app/img/gifs/mCBXa_match_transforms.gif)

* _Match Translate_ - Matches the translation attributes.
![match_translate](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/0_app/img/gifs/mCBXa_match_translate.gif)

* _Match Rotate_ - Matches the rotation attributes.
![match_rotate](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/0_app/img/gifs/mCBXa_match_rotate.gif)

* _Match Scale_ - Matches the scale attributes.
![match_scale](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/0_app/img/gifs/mCBXa_match_scale.gif)



### **Connect Attributes**
* _Connect Attributes_ - Connects attributes of subsequent object selection to first selection. Similar to the _Reset Channels_ tool, if channelbox attributes are highlighted only those attributes will be connected.
* _Disconnect Attributes_ - Disconnects connected attributes. If attributes are highlighted then only those attributes will be disconnected. If no attributes are highlighted then all connected attributes will be disconnected. Note that the Disconnect Attribute tool also works to delete keyed animation on channels.
![connect_attributes](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/0_app/img/gifs/mCBXa_connect_disconnect_attributes.gif)


### **Add Attributes**
* _Add Attribute_ - Add a custom attribute. User provides name and specifies attribute type via the dropdown menu. Attribute Types defaults to 'bool'. Provide a Min/Max value if desired for float or int types. 
![add_attributes](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/0_app/img/gifs/mCBXa_addDel_attr.gif)

* _Add Separator_ - Create a channel box divider. Name provided will be converted to uppercase. If no name is provided an underscored name (ex. ___ ) will be created by default. 
* _Delete Attributes_ - Deletes specified custom attributes. 
![add_separator](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/0_app/img/gifs/mCBXa_add_separator.gif)


### **Channel Attributes**
* _Lock/Unlock Attribute_ -  Works similar to the _Reset Channels_ tool. For selected object(s), lock all attributes. If attributes are already locked the opposite unlock action will be done. If specific attributes are highlighted only those attributes locked/unlocked. 
![lock_unlock_attributes](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/0_app/img/gifs/mCBXa_lockUnlock_attributes.gif)

* _Hide Attribute_ - For selected object(s), hides selected attributes.
![hide_attributes](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/0_app/img/gifs/mCBXa_hide_attributes.gif)

* _Lock + Hide Attribute_ - For selected object(s), lock and hide all attributes. Toggles unlocked and unhidden if action initialized again. If specific attributes are highlighted only those attributes affected. 
**Note**, a current bug exists where re-initializing action on specified attributes does not unlock and unhide the attributes as seen in the example gif: 
![lock_unlock_attributes](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/0_app/img/gifs/mCBXa_lockHide_unlockUnhide_attributes.gif)

* _Keyable/Unkeyable Attribute_ - For selected object(s), makes all attributes keyable. Toggles attributes unkeyable if action initialized again. If specific attributes are highlighted only those attributes affected. 
![keyable_unkeyable_attribute](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/0_app/img/gifs/mCBXa_keyableUnkeyable_attributes.gif)

* _Mute/Unmute Attribute_ - For selected object(s), mutes keyed attributes. **Note** that animation needs to be present on attributes for action to be applied. Toggles attributes unmute if action initialized again. If specific attributes are highlighted only those attributes affected. 
**Note** - The _Mute_ and _Unmute_ tool have been split into separate buttons in order to get it to work.
![mute_unmute_attributes](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/0_app/img/gifs/mCBXa_mute_unmute_attributes.gif)

* ^ _(Reorder Attribute - Up)_
* v _(Reorder Attribute - Down)_


### **HELP**
* _Help_ - Opens the Wiki Help page (_hey, that's this page here!_). 

![help](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/0_app/img/gifs/mCBXa_help.gif)




## Installation Instructions
### **Launching Through the Maya Shelf** 
1. Download the App modules and place them in your script's path.
![app_module_download](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/0_app/img/instructions_screengrabs/app_modules_folder.png)

2. Download the Maya shelf and icon for the tool. 
![maya_prefs_shelf_folder](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/0_app/img/instructions_screengrabs/app_shelf_folder.png)
![maya_shelf_folder](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/0_app/img/instructions_screengrabs/app_shelf_folder.png)

3. Place the icon into the Maya prefs icon folder C:\Users\<user>\OneDrive\Documents\maya\<version>\prefs\icons
![maya_prefs_icon_folder](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/0_app/img/instructions_screengrabs/maya_prefs_icon.png)
![maya_icon_folder](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/0_app/img/instructions_screengrabs/maya_icon_folder.png)

4. Place the shelf into the Maya prefs shelf folder C:\Users\<user>\OneDrive\Documents\maya\<version>\prefs\shelves
![maya_prefs_shelf_folder](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/0_app/img/instructions_screengrabs/maya_prefs_shelves.png)
![maya_shelf_folder](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/0_app/img/instructions_screengrabs/maya_shelf_folder.png)

5. Launch Maya > On the Maya shelf you will see a new 'user' shelf with the Modify ChannelBox Tool present

     *_Reconnection of the icon path may be required in Maya's Shelf Editor_

6. Click to launch the tool. 
![launch_ui](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/img/gif/launch_shelf_ui.gif)

### **Launching Via Code** 
Alternatively, the user can launch the tool by calling the tool's module via code:
1. Download the app's modules
![download_modules](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/0_app/img/instructions_screengrabs/app_modules_folder.png)
![cmd_line_launch_ui](https://github.com/g33cheese/modify-channelbox-attributes/blob/main/0_app/img/instructions_screengrabs/launch_cmdline_ui.gif)

2. Place the app modules into your scripts path
3. In your Maya command line or script editor execute the following code:

`import ui`

`ui.load()`

