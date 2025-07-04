# Documentation for Little Green Light

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to */api*

| Class | Method | HTTP request | Description |
|------------ | ------------- | ------------- | -------------|
| *AppealRequestsApi* | [**lglApiV1AppealRequestsCreate**](Apis/AppealRequestsApi.md#lglapiv1appealrequestscreate) | **POST** /v1/appeals/{appeal_id}/appeal_requests.json | Create new Appeal Request |
*AppealRequestsApi* | [**lglApiV1AppealRequestsDestroy**](Apis/AppealRequestsApi.md#lglapiv1appealrequestsdestroy) | **DELETE** /v1/appeal_requests/{id}.json | Delete Appeal Request |
*AppealRequestsApi* | [**lglApiV1AppealRequestsUpdate**](Apis/AppealRequestsApi.md#lglapiv1appealrequestsupdate) | **PATCH** /v1/appeal_requests/{id}.json | Update Appeal Request |
*AppealRequestsApi* | [**v1AppealAppealRequests**](Apis/AppealRequestsApi.md#v1appealappealrequests) | **GET** /v1/appeals/{appeal_id}/appeal_requests.json | Fetch Appeal Requests for Appeal |
*AppealRequestsApi* | [**v1AppealRequest**](Apis/AppealRequestsApi.md#v1appealrequest) | **GET** /v1/appeal_requests/{id}.json | Show Appeal Request details |
*AppealRequestsApi* | [**v1ConstituentAppealRequests**](Apis/AppealRequestsApi.md#v1constituentappealrequests) | **GET** /v1/constituents/{constituent_id}/appeal_requests.json | Fetch Appeal Requests for Constituent |
*AppealRequestsApi* | [**v1CreateAppealRequestV1ConstituentAppealRequests**](Apis/AppealRequestsApi.md#v1createappealrequestv1constituentappealrequests) | **POST** /v1/constituents/{constituent_id}/appeal_requests.json | Create new Appeal Request for Constituent |
| *AppealsApi* | [**v1Appeals**](Apis/AppealsApi.md#v1appeals) | **GET** /v1/appeals.json | Fetch Appeals |
| *AttributesApi* | [**v1Attributes**](Apis/AttributesApi.md#v1attributes) | **GET** /v1/attributes.json | Fetch Custom Attributes |
| *CampaignsApi* | [**v1Campaigns**](Apis/CampaignsApi.md#v1campaigns) | **GET** /v1/campaigns.json | Fetch Campaigns |
| *CategoriesApi* | [**lglApiV1CategoriesCreate**](Apis/CategoriesApi.md#lglapiv1categoriescreate) | **POST** /v1/categories.json | Create new Category |
*CategoriesApi* | [**lglApiV1CategoriesDestroy**](Apis/CategoriesApi.md#lglapiv1categoriesdestroy) | **DELETE** /v1/categories/{id}.json | Delete Category |
*CategoriesApi* | [**lglApiV1CategoriesUpdate**](Apis/CategoriesApi.md#lglapiv1categoriesupdate) | **PATCH** /v1/categories/{id}.json | Update Category |
*CategoriesApi* | [**v1Categories**](Apis/CategoriesApi.md#v1categories) | **GET** /v1/categories.json | Fetch Categories for Account |
*CategoriesApi* | [**v1Category**](Apis/CategoriesApi.md#v1category) | **GET** /v1/categories/{id}.json | Show Category details |
*CategoriesApi* | [**v1ConstituentCategories**](Apis/CategoriesApi.md#v1constituentcategories) | **GET** /v1/constituents/{constituent_id}/categories.json | Fetch Categories for Constituent |
| *ClassAffiliationTypesApi* | [**v1ClassAffiliationTypes**](Apis/ClassAffiliationTypesApi.md#v1classaffiliationtypes) | **GET** /v1/class_affiliation_types.json | Fetch Class Affiliation Types |
| *ClassAffiliationsApi* | [**lglApiV1ClassAffiliationsCreate**](Apis/ClassAffiliationsApi.md#lglapiv1classaffiliationscreate) | **POST** /v1/constituents/{constituent_id}/class_affiliations.json | Create new Class Affiliation |
*ClassAffiliationsApi* | [**lglApiV1ClassAffiliationsDestroy**](Apis/ClassAffiliationsApi.md#lglapiv1classaffiliationsdestroy) | **DELETE** /v1/class_affiliations/{id}.json | Delete Class Affiliation |
*ClassAffiliationsApi* | [**lglApiV1ClassAffiliationsUpdate**](Apis/ClassAffiliationsApi.md#lglapiv1classaffiliationsupdate) | **PATCH** /v1/class_affiliations/{id}.json | Update Class Affiliation |
*ClassAffiliationsApi* | [**v1ClassAffiliation**](Apis/ClassAffiliationsApi.md#v1classaffiliation) | **GET** /v1/class_affiliations/{id}.json | Show Class Affiliation details |
*ClassAffiliationsApi* | [**v1ConstituentClassAffiliations**](Apis/ClassAffiliationsApi.md#v1constituentclassaffiliations) | **GET** /v1/constituents/{constituent_id}/class_affiliations.json | Fetch Class Affiliations |
| *ConstituentRelationshipsApi* | [**lglApiV1ConstituentRelationshipsCreate**](Apis/ConstituentRelationshipsApi.md#lglapiv1constituentrelationshipscreate) | **POST** /v1/constituents/{constituent_id}/constituent_relationships.json | Create new Constituent Relationship |
*ConstituentRelationshipsApi* | [**lglApiV1ConstituentRelationshipsDestroy**](Apis/ConstituentRelationshipsApi.md#lglapiv1constituentrelationshipsdestroy) | **DELETE** /v1/constituent_relationships/{id}.json | Delete Constituent Relationship |
*ConstituentRelationshipsApi* | [**lglApiV1ConstituentRelationshipsUpdate**](Apis/ConstituentRelationshipsApi.md#lglapiv1constituentrelationshipsupdate) | **PATCH** /v1/constituent_relationships/{id}.json | Update Constituent Relationship |
*ConstituentRelationshipsApi* | [**v1ConstituentConstituentRelationships**](Apis/ConstituentRelationshipsApi.md#v1constituentconstituentrelationships) | **GET** /v1/constituents/{constituent_id}/constituent_relationships.json | Fetch Constituent Relationships for a Constituent |
*ConstituentRelationshipsApi* | [**v1ConstituentRelationship**](Apis/ConstituentRelationshipsApi.md#v1constituentrelationship) | **GET** /v1/constituent_relationships/{id}.json | Show Constituent Relationship details |
| *ConstituentsApi* | [**lglApiV1ConstituentsCreate**](Apis/ConstituentsApi.md#lglapiv1constituentscreate) | **POST** /v1/constituents.json | Create new Constituent |
*ConstituentsApi* | [**lglApiV1ConstituentsDestroy**](Apis/ConstituentsApi.md#lglapiv1constituentsdestroy) | **DELETE** /v1/constituents/{id}.json | Delete constituent |
*ConstituentsApi* | [**lglApiV1ConstituentsUpdate**](Apis/ConstituentsApi.md#lglapiv1constituentsupdate) | **PATCH** /v1/constituents/{id}.json | Update constituent |
*ConstituentsApi* | [**searchV1Constituents**](Apis/ConstituentsApi.md#searchv1constituents) | **GET** /v1/constituents/search.json | Search for Constituents |
*ConstituentsApi* | [**v1Constituent**](Apis/ConstituentsApi.md#v1constituent) | **GET** /v1/constituents/{id}.json | Show Constituent details |
*ConstituentsApi* | [**v1Constituents**](Apis/ConstituentsApi.md#v1constituents) | **GET** /v1/constituents.json | Fetch all Constituents for an account |
| *ContactReportsApi* | [**lglApiV1ContactReportsCreate**](Apis/ContactReportsApi.md#lglapiv1contactreportscreate) | **POST** /v1/constituents/{constituent_id}/contact_reports.json | Create new Contact Report |
*ContactReportsApi* | [**lglApiV1ContactReportsDestroy**](Apis/ContactReportsApi.md#lglapiv1contactreportsdestroy) | **DELETE** /v1/contact_reports/{id}.json | Delete Contact Report |
*ContactReportsApi* | [**lglApiV1ContactReportsUpdate**](Apis/ContactReportsApi.md#lglapiv1contactreportsupdate) | **PATCH** /v1/contact_reports/{id}.json | Update Contact Report |
*ContactReportsApi* | [**searchV1ContactReports**](Apis/ContactReportsApi.md#searchv1contactreports) | **GET** /v1/contact_reports/search.json | Search for Contact Reports |
*ContactReportsApi* | [**v1ConstituentContactReports**](Apis/ContactReportsApi.md#v1constituentcontactreports) | **GET** /v1/constituents/{constituent_id}/contact_reports.json | Fetch Contact Reports for Constituent |
*ContactReportsApi* | [**v1ContactReport**](Apis/ContactReportsApi.md#v1contactreport) | **GET** /v1/contact_reports/{id}.json | Show Contact Report details |
*ContactReportsApi* | [**v1ContactReports**](Apis/ContactReportsApi.md#v1contactreports) | **GET** /v1/contact_reports.json | Fetch Contact Reports for Account |
| *EmailAddressesApi* | [**lglApiV1EmailAddressesCreate**](Apis/EmailAddressesApi.md#lglapiv1emailaddressescreate) | **POST** /v1/constituents/{constituent_id}/email_addresses.json | Create new Email Address |
*EmailAddressesApi* | [**lglApiV1EmailAddressesDestroy**](Apis/EmailAddressesApi.md#lglapiv1emailaddressesdestroy) | **DELETE** /v1/email_addresses/{id}.json | Delete Email Address |
*EmailAddressesApi* | [**lglApiV1EmailAddressesUpdate**](Apis/EmailAddressesApi.md#lglapiv1emailaddressesupdate) | **PATCH** /v1/email_addresses/{id}.json | Update Email Address |
*EmailAddressesApi* | [**v1ConstituentEmailAddresses**](Apis/EmailAddressesApi.md#v1constituentemailaddresses) | **GET** /v1/constituents/{constituent_id}/email_addresses.json | Fetch Email Addresses |
*EmailAddressesApi* | [**v1EmailAddress**](Apis/EmailAddressesApi.md#v1emailaddress) | **GET** /v1/email_addresses/{id}.json | Show Email Address details |
| *EventsApi* | [**v1Events**](Apis/EventsApi.md#v1events) | **GET** /v1/events.json | Fetch Events |
| *FundsApi* | [**v1Funds**](Apis/FundsApi.md#v1funds) | **GET** /v1/funds.json | Fetch Funds |
| *GiftCategoriesApi* | [**v1GiftCategories**](Apis/GiftCategoriesApi.md#v1giftcategories) | **GET** /v1/gift_categories.json | Fetch Gift Categories |
| *GiftTypesApi* | [**v1GiftTypes**](Apis/GiftTypesApi.md#v1gifttypes) | **GET** /v1/gift_types.json | Fetch Gift Types |
| *GiftsApi* | [**lglApiV1GiftsCreate**](Apis/GiftsApi.md#lglapiv1giftscreate) | **POST** /v1/constituents/{constituent_id}/gifts.json | Create new Gift |
*GiftsApi* | [**lglApiV1GiftsDestroy**](Apis/GiftsApi.md#lglapiv1giftsdestroy) | **DELETE** /v1/gifts/{id}.json | Delete Gift |
*GiftsApi* | [**lglApiV1GiftsUpdate**](Apis/GiftsApi.md#lglapiv1giftsupdate) | **PATCH** /v1/gifts/{id}.json | Update Gift |
*GiftsApi* | [**searchV1Gifts**](Apis/GiftsApi.md#searchv1gifts) | **GET** /v1/gifts/search.json | Search for Gifts |
*GiftsApi* | [**v1ConstituentGifts**](Apis/GiftsApi.md#v1constituentgifts) | **GET** /v1/constituents/{constituent_id}/gifts.json | Fetch Gifts |
*GiftsApi* | [**v1Gift**](Apis/GiftsApi.md#v1gift) | **GET** /v1/gifts/{id}.json | Show Gift details |
| *GroupMembershipsApi* | [**lglApiV1GroupMembershipsCreate**](Apis/GroupMembershipsApi.md#lglapiv1groupmembershipscreate) | **POST** /v1/constituents/{constituent_id}/group_memberships.json | Create new Group Membership |
*GroupMembershipsApi* | [**lglApiV1GroupMembershipsDestroy**](Apis/GroupMembershipsApi.md#lglapiv1groupmembershipsdestroy) | **DELETE** /v1/group_memberships/{id}.json | Delete Group Membership |
*GroupMembershipsApi* | [**lglApiV1GroupMembershipsUpdate**](Apis/GroupMembershipsApi.md#lglapiv1groupmembershipsupdate) | **PATCH** /v1/group_memberships/{id}.json | Update Group Membership |
*GroupMembershipsApi* | [**v1ConstituentGroupMemberships**](Apis/GroupMembershipsApi.md#v1constituentgroupmemberships) | **GET** /v1/constituents/{constituent_id}/group_memberships.json | Fetch Group Memberships |
*GroupMembershipsApi* | [**v1GroupMembership**](Apis/GroupMembershipsApi.md#v1groupmembership) | **GET** /v1/group_memberships/{id}.json | Show Group Membership details |
| *GroupsApi* | [**lglApiV1GroupsCreate**](Apis/GroupsApi.md#lglapiv1groupscreate) | **POST** /v1/groups.json | Create new Group |
*GroupsApi* | [**lglApiV1GroupsDestroy**](Apis/GroupsApi.md#lglapiv1groupsdestroy) | **DELETE** /v1/groups/{id}.json | Delete Group |
*GroupsApi* | [**lglApiV1GroupsUpdate**](Apis/GroupsApi.md#lglapiv1groupsupdate) | **PATCH** /v1/groups/{id}.json | Update Group |
*GroupsApi* | [**v1Group**](Apis/GroupsApi.md#v1group) | **GET** /v1/groups/{id}.json | Show Group details |
*GroupsApi* | [**v1Groups**](Apis/GroupsApi.md#v1groups) | **GET** /v1/groups.json | Fetch Groups |
| *InvitationsApi* | [**lglApiV1InvitationsCreate**](Apis/InvitationsApi.md#lglapiv1invitationscreate) | **POST** /v1/events/{event_id}/invitations.json | Create new Invitation |
*InvitationsApi* | [**lglApiV1InvitationsDestroy**](Apis/InvitationsApi.md#lglapiv1invitationsdestroy) | **DELETE** /v1/invitations/{id}.json | Delete Invitation |
*InvitationsApi* | [**lglApiV1InvitationsUpdate**](Apis/InvitationsApi.md#lglapiv1invitationsupdate) | **PATCH** /v1/invitations/{id}.json | Update Invitation |
*InvitationsApi* | [**v1ConstituentInvitations**](Apis/InvitationsApi.md#v1constituentinvitations) | **GET** /v1/constituents/{constituent_id}/invitations.json | Fetch Invitations for Constituent |
*InvitationsApi* | [**v1CreateInvitationV1ConstituentInvitations**](Apis/InvitationsApi.md#v1createinvitationv1constituentinvitations) | **POST** /v1/constituents/{constituent_id}/invitations.json | Create new Invitation for Constituent |
*InvitationsApi* | [**v1EventInvitations**](Apis/InvitationsApi.md#v1eventinvitations) | **GET** /v1/events/{event_id}/invitations.json | Fetch Invitations for Event |
*InvitationsApi* | [**v1Invitation**](Apis/InvitationsApi.md#v1invitation) | **GET** /v1/invitations/{id}.json | Show Invitation details |
| *KeywordsApi* | [**lglApiV1KeywordsCreate**](Apis/KeywordsApi.md#lglapiv1keywordscreate) | **POST** /v1/categories/{category_id}/keywords.json | Create new Keyword |
*KeywordsApi* | [**lglApiV1KeywordsDestroy**](Apis/KeywordsApi.md#lglapiv1keywordsdestroy) | **DELETE** /v1/keywords/{id}.json | Delete Keyword |
*KeywordsApi* | [**lglApiV1KeywordsUpdate**](Apis/KeywordsApi.md#lglapiv1keywordsupdate) | **PATCH** /v1/keywords/{id}.json | Update Keyword |
*KeywordsApi* | [**v1CategoryKeywords**](Apis/KeywordsApi.md#v1categorykeywords) | **GET** /v1/categories/{category_id}/keywords.json | Fetch Keywords |
*KeywordsApi* | [**v1ConstituentKeyword**](Apis/KeywordsApi.md#v1constituentkeyword) | **DELETE** /v1/constituents/{constituent_id}/keywords/{id}.json | Remove Keyword |
*KeywordsApi* | [**v1ConstituentKeywords**](Apis/KeywordsApi.md#v1constituentkeywords) | **POST** /v1/constituents/{constituent_id}/keywords.json | Add Keyword |
*KeywordsApi* | [**v1Keyword**](Apis/KeywordsApi.md#v1keyword) | **GET** /v1/keywords/{id}.json | Show Keyword details |
| *MailingTemplatesApi* | [**v1MailingTemplates**](Apis/MailingTemplatesApi.md#v1mailingtemplates) | **GET** /v1/mailing_templates.json | Fetch Mailing Templates |
| *MembershipLevelsApi* | [**lglApiV1MembershipLevelsCreate**](Apis/MembershipLevelsApi.md#lglapiv1membershiplevelscreate) | **POST** /v1/membership_levels.json | Create new Membership Level |
*MembershipLevelsApi* | [**lglApiV1MembershipLevelsDestroy**](Apis/MembershipLevelsApi.md#lglapiv1membershiplevelsdestroy) | **DELETE** /v1/membership_levels/{id}.json | Delete Membership Level |
*MembershipLevelsApi* | [**lglApiV1MembershipLevelsUpdate**](Apis/MembershipLevelsApi.md#lglapiv1membershiplevelsupdate) | **PATCH** /v1/membership_levels/{id}.json | Update Membership Level |
*MembershipLevelsApi* | [**v1MembershipLevel**](Apis/MembershipLevelsApi.md#v1membershiplevel) | **GET** /v1/membership_levels/{id}.json | Show Membership Level details |
*MembershipLevelsApi* | [**v1MembershipLevels**](Apis/MembershipLevelsApi.md#v1membershiplevels) | **GET** /v1/membership_levels.json | Fetch Membership Levels |
| *MembershipsApi* | [**lglApiV1MembershipsCreate**](Apis/MembershipsApi.md#lglapiv1membershipscreate) | **POST** /v1/constituents/{constituent_id}/memberships.json | Create new Membership |
*MembershipsApi* | [**lglApiV1MembershipsDestroy**](Apis/MembershipsApi.md#lglapiv1membershipsdestroy) | **DELETE** /v1/memberships/{id}.json | Delete Membership |
*MembershipsApi* | [**lglApiV1MembershipsUpdate**](Apis/MembershipsApi.md#lglapiv1membershipsupdate) | **PATCH** /v1/memberships/{id}.json | Update Membership |
*MembershipsApi* | [**v1ConstituentMemberships**](Apis/MembershipsApi.md#v1constituentmemberships) | **GET** /v1/constituents/{constituent_id}/memberships.json | Fetch Memberships |
*MembershipsApi* | [**v1Membership**](Apis/MembershipsApi.md#v1membership) | **GET** /v1/memberships/{id}.json | Show Membership details |
| *NotesApi* | [**lglApiV1NotesCreate**](Apis/NotesApi.md#lglapiv1notescreate) | **POST** /v1/constituents/{constituent_id}/notes.json | Create new Note |
*NotesApi* | [**lglApiV1NotesDestroy**](Apis/NotesApi.md#lglapiv1notesdestroy) | **DELETE** /v1/notes/{id}.json | Delete Note |
*NotesApi* | [**lglApiV1NotesUpdate**](Apis/NotesApi.md#lglapiv1notesupdate) | **PATCH** /v1/notes/{id}.json | Update Note |
*NotesApi* | [**v1ConstituentNotes**](Apis/NotesApi.md#v1constituentnotes) | **GET** /v1/constituents/{constituent_id}/notes.json | Fetch Notes for Constituent |
*NotesApi* | [**v1Note**](Apis/NotesApi.md#v1note) | **GET** /v1/notes/{id}.json | Show Note details |
*NotesApi* | [**v1Notes**](Apis/NotesApi.md#v1notes) | **GET** /v1/notes.json | Fetch Notes for Account |
| *PaymentTypesApi* | [**v1PaymentTypes**](Apis/PaymentTypesApi.md#v1paymenttypes) | **GET** /v1/payment_types.json | Fetch Payment Types |
| *PhoneNumbersApi* | [**lglApiV1PhoneNumbersCreate**](Apis/PhoneNumbersApi.md#lglapiv1phonenumberscreate) | **POST** /v1/constituents/{constituent_id}/phone_numbers.json | Create new Phone Number |
*PhoneNumbersApi* | [**lglApiV1PhoneNumbersDestroy**](Apis/PhoneNumbersApi.md#lglapiv1phonenumbersdestroy) | **DELETE** /v1/phone_numbers/{id}.json | Delete Phone Number |
*PhoneNumbersApi* | [**lglApiV1PhoneNumbersUpdate**](Apis/PhoneNumbersApi.md#lglapiv1phonenumbersupdate) | **PATCH** /v1/phone_numbers/{id}.json | Update Phone Number |
*PhoneNumbersApi* | [**v1ConstituentPhoneNumbers**](Apis/PhoneNumbersApi.md#v1constituentphonenumbers) | **GET** /v1/constituents/{constituent_id}/phone_numbers.json | Fetch Phone Numbers |
*PhoneNumbersApi* | [**v1PhoneNumber**](Apis/PhoneNumbersApi.md#v1phonenumber) | **GET** /v1/phone_numbers/{id}.json | Show Phone Number details |
| *RelationshipTypesApi* | [**v1RelationshipTypes**](Apis/RelationshipTypesApi.md#v1relationshiptypes) | **GET** /v1/relationship_types.json | Fetch Relationship Types |
| *StreetAddressesApi* | [**lglApiV1StreetAddressesCreate**](Apis/StreetAddressesApi.md#lglapiv1streetaddressescreate) | **POST** /v1/constituents/{constituent_id}/street_addresses.json | Create new Street Address |
*StreetAddressesApi* | [**lglApiV1StreetAddressesDestroy**](Apis/StreetAddressesApi.md#lglapiv1streetaddressesdestroy) | **DELETE** /v1/street_addresses/{id}.json | Delete Street Address |
*StreetAddressesApi* | [**lglApiV1StreetAddressesUpdate**](Apis/StreetAddressesApi.md#lglapiv1streetaddressesupdate) | **PATCH** /v1/street_addresses/{id}.json | Update Street Address |
*StreetAddressesApi* | [**v1ConstituentStreetAddresses**](Apis/StreetAddressesApi.md#v1constituentstreetaddresses) | **GET** /v1/constituents/{constituent_id}/street_addresses.json | Fetch Street Addresses |
*StreetAddressesApi* | [**v1StreetAddress**](Apis/StreetAddressesApi.md#v1streetaddress) | **GET** /v1/street_addresses/{id}.json | Show Street Address details |
| *TeamMembersApi* | [**v1TeamMembers**](Apis/TeamMembersApi.md#v1teammembers) | **GET** /v1/team_members.json | Fetch Team Members |
| *TypesApi* | [**v1Types**](Apis/TypesApi.md#v1types) | **GET** /v1/types.json | Fetch Types for Account |
*TypesApi* | [**v1V1TypesType**](Apis/TypesApi.md#v1v1typestype) | **GET** /v1/types/{type}.json | Fetch Values for Type |
| *VolunteerTimesApi* | [**lglApiV1VolunteerTimesCreate**](Apis/VolunteerTimesApi.md#lglapiv1volunteertimescreate) | **POST** /v1/constituents/{constituent_id}/volunteer_times.json | Create new Volunteer Time |
*VolunteerTimesApi* | [**lglApiV1VolunteerTimesDestroy**](Apis/VolunteerTimesApi.md#lglapiv1volunteertimesdestroy) | **DELETE** /v1/volunteer_times/{id}.json | Delete Volunteer Time |
*VolunteerTimesApi* | [**lglApiV1VolunteerTimesUpdate**](Apis/VolunteerTimesApi.md#lglapiv1volunteertimesupdate) | **PATCH** /v1/volunteer_times/{id}.json | Update Volunteer Time |
*VolunteerTimesApi* | [**searchV1VolunteerTimes**](Apis/VolunteerTimesApi.md#searchv1volunteertimes) | **GET** /v1/volunteer_times/search.json | Search for Volunteer Times |
*VolunteerTimesApi* | [**v1ConstituentVolunteerTimes**](Apis/VolunteerTimesApi.md#v1constituentvolunteertimes) | **GET** /v1/constituents/{constituent_id}/volunteer_times.json | Fetch Volunteer Times for Constituent |
*VolunteerTimesApi* | [**v1VolunteerTime**](Apis/VolunteerTimesApi.md#v1volunteertime) | **GET** /v1/volunteer_times/{id}.json | Show Volunteer Time details |
*VolunteerTimesApi* | [**v1VolunteerTimes**](Apis/VolunteerTimesApi.md#v1volunteertimes) | **GET** /v1/volunteer_times.json | Fetch Volunteer Times for Account |
| *WebAddressesApi* | [**lglApiV1WebAddressesCreate**](Apis/WebAddressesApi.md#lglapiv1webaddressescreate) | **POST** /v1/constituents/{constituent_id}/web_addresses.json | Create new Web Address |
*WebAddressesApi* | [**lglApiV1WebAddressesDestroy**](Apis/WebAddressesApi.md#lglapiv1webaddressesdestroy) | **DELETE** /v1/web_addresses/{id}.json | Delete Web Address |
*WebAddressesApi* | [**lglApiV1WebAddressesUpdate**](Apis/WebAddressesApi.md#lglapiv1webaddressesupdate) | **PATCH** /v1/web_addresses/{id}.json | Update Web Address |
*WebAddressesApi* | [**v1ConstituentWebAddresses**](Apis/WebAddressesApi.md#v1constituentwebaddresses) | **GET** /v1/constituents/{constituent_id}/web_addresses.json | Fetch Web Addresses |
*WebAddressesApi* | [**v1WebAddress**](Apis/WebAddressesApi.md#v1webaddress) | **GET** /v1/web_addresses/{id}.json | Show Web Address details |


<a name="documentation-for-models"></a>
## Documentation for Models

 - [AddBody](./Models/AddBody.md)
 - [Appeal](./Models/Appeal.md)
 - [AppealAggregatedResponse](./Models/AppealAggregatedResponse.md)
 - [AppealRequest](./Models/AppealRequest.md)
 - [AppealRequestAggregatedResponse](./Models/AppealRequestAggregatedResponse.md)
 - [AppealRequestResponse](./Models/AppealRequestResponse.md)
 - [AppealRequestUpdate](./Models/AppealRequestUpdate.md)
 - [AppealRequests_index](./Models/AppealRequests_index.md)
 - [AppealRequests_show](./Models/AppealRequests_show.md)
 - [AppealResponse](./Models/AppealResponse.md)
 - [AppealUpdate](./Models/AppealUpdate.md)
 - [Appeals_index](./Models/Appeals_index.md)
 - [Appeals_show](./Models/Appeals_show.md)
 - [Attendance](./Models/Attendance.md)
 - [Attendance_create](./Models/Attendance_create.md)
 - [Attribute](./Models/Attribute.md)
 - [AttributeAggregatedResponse](./Models/AttributeAggregatedResponse.md)
 - [AttributeResponse](./Models/AttributeResponse.md)
 - [AttributeUpdate](./Models/AttributeUpdate.md)
 - [Attributes_index](./Models/Attributes_index.md)
 - [Attributes_show](./Models/Attributes_show.md)
 - [Campaign](./Models/Campaign.md)
 - [CampaignAggregatedResponse](./Models/CampaignAggregatedResponse.md)
 - [CampaignResponse](./Models/CampaignResponse.md)
 - [CampaignUpdate](./Models/CampaignUpdate.md)
 - [Campaigns_index](./Models/Campaigns_index.md)
 - [Campaigns_show](./Models/Campaigns_show.md)
 - [Categories_index](./Models/Categories_index.md)
 - [Categories_show](./Models/Categories_show.md)
 - [Category](./Models/Category.md)
 - [CategoryAggregatedCreate](./Models/CategoryAggregatedCreate.md)
 - [CategoryAggregatedUpdate](./Models/CategoryAggregatedUpdate.md)
 - [ClassAffiliation](./Models/ClassAffiliation.md)
 - [ClassAffiliationAggregatedResponse](./Models/ClassAffiliationAggregatedResponse.md)
 - [ClassAffiliationResponse](./Models/ClassAffiliationResponse.md)
 - [ClassAffiliationType](./Models/ClassAffiliationType.md)
 - [ClassAffiliationTypeAggregatedResponse](./Models/ClassAffiliationTypeAggregatedResponse.md)
 - [ClassAffiliationTypeResponse](./Models/ClassAffiliationTypeResponse.md)
 - [ClassAffiliationTypeUpdate](./Models/ClassAffiliationTypeUpdate.md)
 - [ClassAffiliationTypes_index](./Models/ClassAffiliationTypes_index.md)
 - [ClassAffiliationTypes_show](./Models/ClassAffiliationTypes_show.md)
 - [ClassAffiliationUpdate](./Models/ClassAffiliationUpdate.md)
 - [ClassAffiliations_index](./Models/ClassAffiliations_index.md)
 - [ClassAffiliations_show](./Models/ClassAffiliations_show.md)
 - [Constituent](./Models/Constituent.md)
 - [ConstituentAggregatedResponse](./Models/ConstituentAggregatedResponse.md)
 - [ConstituentRelationship](./Models/ConstituentRelationship.md)
 - [ConstituentRelationshipAggregatedResponse](./Models/ConstituentRelationshipAggregatedResponse.md)
 - [ConstituentRelationshipResponse](./Models/ConstituentRelationshipResponse.md)
 - [ConstituentRelationshipUpdate](./Models/ConstituentRelationshipUpdate.md)
 - [ConstituentRelationships_index](./Models/ConstituentRelationships_index.md)
 - [ConstituentRelationships_show](./Models/ConstituentRelationships_show.md)
 - [ConstituentResponse](./Models/ConstituentResponse.md)
 - [ConstituentResponseIndex](./Models/ConstituentResponseIndex.md)
 - [ConstituentUpdate](./Models/ConstituentUpdate.md)
 - [Constituents_index](./Models/Constituents_index.md)
 - [Constituents_show](./Models/Constituents_show.md)
 - [ContactReport](./Models/ContactReport.md)
 - [ContactReportAggregatedResponse](./Models/ContactReportAggregatedResponse.md)
 - [ContactReportResponse](./Models/ContactReportResponse.md)
 - [ContactReportUpdate](./Models/ContactReportUpdate.md)
 - [ContactReports_index](./Models/ContactReports_index.md)
 - [ContactReports_show](./Models/ContactReports_show.md)
 - [CreateBody](./Models/CreateBody.md)
 - [CreateBody_Const](./Models/CreateBody_Const.md)
 - [CustomAttr](./Models/CustomAttr.md)
 - [CustomAttr_create](./Models/CustomAttr_create.md)
 - [CustomAttr_index](./Models/CustomAttr_index.md)
 - [CustomAttr_show](./Models/CustomAttr_show.md)
 - [CustomField](./Models/CustomField.md)
 - [CustomFieldAggregatedUpdate](./Models/CustomFieldAggregatedUpdate.md)
 - [CustomFields_index](./Models/CustomFields_index.md)
 - [CustomFields_show](./Models/CustomFields_show.md)
 - [CustomValue](./Models/CustomValue.md)
 - [CustomValueAggregatedResponse](./Models/CustomValueAggregatedResponse.md)
 - [CustomValueAggregatedUpdate](./Models/CustomValueAggregatedUpdate.md)
 - [CustomValueResponse](./Models/CustomValueResponse.md)
 - [CustomValueUpdate](./Models/CustomValueUpdate.md)
 - [EmailAddress](./Models/EmailAddress.md)
 - [EmailAddressAggregatedResponse](./Models/EmailAddressAggregatedResponse.md)
 - [EmailAddressResponse](./Models/EmailAddressResponse.md)
 - [EmailAddressUpdate](./Models/EmailAddressUpdate.md)
 - [EmailAddresses_index](./Models/EmailAddresses_index.md)
 - [EmailAddresses_show](./Models/EmailAddresses_show.md)
 - [Event](./Models/Event.md)
 - [EventAggregatedResponse](./Models/EventAggregatedResponse.md)
 - [EventResponse](./Models/EventResponse.md)
 - [EventUpdate](./Models/EventUpdate.md)
 - [Events_index](./Models/Events_index.md)
 - [Events_show](./Models/Events_show.md)
 - [Fund](./Models/Fund.md)
 - [FundAggregatedResponse](./Models/FundAggregatedResponse.md)
 - [FundResponse](./Models/FundResponse.md)
 - [FundUpdate](./Models/FundUpdate.md)
 - [Funds_index](./Models/Funds_index.md)
 - [Funds_show](./Models/Funds_show.md)
 - [Gift](./Models/Gift.md)
 - [GiftAggregatedResponse](./Models/GiftAggregatedResponse.md)
 - [GiftCategories_index](./Models/GiftCategories_index.md)
 - [GiftCategories_show](./Models/GiftCategories_show.md)
 - [GiftCategory](./Models/GiftCategory.md)
 - [GiftCategoryAggregatedResponse](./Models/GiftCategoryAggregatedResponse.md)
 - [GiftCategoryResponse](./Models/GiftCategoryResponse.md)
 - [GiftCategoryUpdate](./Models/GiftCategoryUpdate.md)
 - [GiftResponse](./Models/GiftResponse.md)
 - [GiftType](./Models/GiftType.md)
 - [GiftTypeAggregatedResponse](./Models/GiftTypeAggregatedResponse.md)
 - [GiftTypeResponse](./Models/GiftTypeResponse.md)
 - [GiftTypeUpdate](./Models/GiftTypeUpdate.md)
 - [GiftTypes_index](./Models/GiftTypes_index.md)
 - [GiftTypes_show](./Models/GiftTypes_show.md)
 - [GiftUpdate](./Models/GiftUpdate.md)
 - [Gifts_index](./Models/Gifts_index.md)
 - [Gifts_show](./Models/Gifts_show.md)
 - [Group](./Models/Group.md)
 - [GroupAggregatedResponse](./Models/GroupAggregatedResponse.md)
 - [GroupMembership](./Models/GroupMembership.md)
 - [GroupMembershipAggregatedResponse](./Models/GroupMembershipAggregatedResponse.md)
 - [GroupMembershipResponse](./Models/GroupMembershipResponse.md)
 - [GroupMembershipUpdate](./Models/GroupMembershipUpdate.md)
 - [GroupMemberships_index](./Models/GroupMemberships_index.md)
 - [GroupMemberships_show](./Models/GroupMemberships_show.md)
 - [GroupResponse](./Models/GroupResponse.md)
 - [GroupUpdate](./Models/GroupUpdate.md)
 - [Groups_index](./Models/Groups_index.md)
 - [Groups_show](./Models/Groups_show.md)
 - [Invitation](./Models/Invitation.md)
 - [Invitations_index](./Models/Invitations_index.md)
 - [Invitations_show](./Models/Invitations_show.md)
 - [Keyword](./Models/Keyword.md)
 - [KeywordAggregatedResponse](./Models/KeywordAggregatedResponse.md)
 - [KeywordAggregatedUpdate](./Models/KeywordAggregatedUpdate.md)
 - [KeywordResponse](./Models/KeywordResponse.md)
 - [KeywordUpdate](./Models/KeywordUpdate.md)
 - [Keywords_index](./Models/Keywords_index.md)
 - [Keywords_show](./Models/Keywords_show.md)
 - [MailingTemplate](./Models/MailingTemplate.md)
 - [MailingTemplateAggregatedResponse](./Models/MailingTemplateAggregatedResponse.md)
 - [MailingTemplateResponse](./Models/MailingTemplateResponse.md)
 - [MailingTemplateUpdate](./Models/MailingTemplateUpdate.md)
 - [MailingTemplates_index](./Models/MailingTemplates_index.md)
 - [MailingTemplates_show](./Models/MailingTemplates_show.md)
 - [Membership](./Models/Membership.md)
 - [MembershipAggregatedResponse](./Models/MembershipAggregatedResponse.md)
 - [MembershipLevel](./Models/MembershipLevel.md)
 - [MembershipLevelAggregatedResponse](./Models/MembershipLevelAggregatedResponse.md)
 - [MembershipLevelResponse](./Models/MembershipLevelResponse.md)
 - [MembershipLevelUpdate](./Models/MembershipLevelUpdate.md)
 - [MembershipLevels_index](./Models/MembershipLevels_index.md)
 - [MembershipLevels_show](./Models/MembershipLevels_show.md)
 - [MembershipResponse](./Models/MembershipResponse.md)
 - [MembershipUpdate](./Models/MembershipUpdate.md)
 - [Memberships_index](./Models/Memberships_index.md)
 - [Memberships_show](./Models/Memberships_show.md)
 - [Note](./Models/Note.md)
 - [NoteAggregatedResponse](./Models/NoteAggregatedResponse.md)
 - [NoteResponse](./Models/NoteResponse.md)
 - [NoteUpdate](./Models/NoteUpdate.md)
 - [Notes_index](./Models/Notes_index.md)
 - [Notes_show](./Models/Notes_show.md)
 - [PaymentType](./Models/PaymentType.md)
 - [PaymentTypeAggregatedResponse](./Models/PaymentTypeAggregatedResponse.md)
 - [PaymentTypeResponse](./Models/PaymentTypeResponse.md)
 - [PaymentTypeUpdate](./Models/PaymentTypeUpdate.md)
 - [PaymentTypes_index](./Models/PaymentTypes_index.md)
 - [PaymentTypes_show](./Models/PaymentTypes_show.md)
 - [PhoneNumber](./Models/PhoneNumber.md)
 - [PhoneNumberAggregatedResponse](./Models/PhoneNumberAggregatedResponse.md)
 - [PhoneNumberResponse](./Models/PhoneNumberResponse.md)
 - [PhoneNumberUpdate](./Models/PhoneNumberUpdate.md)
 - [PhoneNumbers_index](./Models/PhoneNumbers_index.md)
 - [PhoneNumbers_show](./Models/PhoneNumbers_show.md)
 - [RelationshipType](./Models/RelationshipType.md)
 - [RelationshipTypeAggregatedResponse](./Models/RelationshipTypeAggregatedResponse.md)
 - [RelationshipTypeResponse](./Models/RelationshipTypeResponse.md)
 - [RelationshipTypeUpdate](./Models/RelationshipTypeUpdate.md)
 - [RelationshipTypes_index](./Models/RelationshipTypes_index.md)
 - [RelationshipTypes_show](./Models/RelationshipTypes_show.md)
 - [School](./Models/School.md)
 - [SchoolAggregatedResponse](./Models/SchoolAggregatedResponse.md)
 - [SchoolResponse](./Models/SchoolResponse.md)
 - [SchoolUpdate](./Models/SchoolUpdate.md)
 - [StreetAddress](./Models/StreetAddress.md)
 - [StreetAddressAggregatedResponse](./Models/StreetAddressAggregatedResponse.md)
 - [StreetAddressResponse](./Models/StreetAddressResponse.md)
 - [StreetAddressUpdate](./Models/StreetAddressUpdate.md)
 - [StreetAddresses_index](./Models/StreetAddresses_index.md)
 - [StreetAddresses_show](./Models/StreetAddresses_show.md)
 - [TeamMember](./Models/TeamMember.md)
 - [TeamMemberAggregatedResponse](./Models/TeamMemberAggregatedResponse.md)
 - [TeamMemberResponse](./Models/TeamMemberResponse.md)
 - [TeamMemberUpdate](./Models/TeamMemberUpdate.md)
 - [TeamMembers_index](./Models/TeamMembers_index.md)
 - [TeamMembers_show](./Models/TeamMembers_show.md)
 - [Type](./Models/Type.md)
 - [TypeValue](./Models/TypeValue.md)
 - [TypeValues_index](./Models/TypeValues_index.md)
 - [Types_index](./Models/Types_index.md)
 - [UpdateBody](./Models/UpdateBody.md)
 - [VolunteerTime](./Models/VolunteerTime.md)
 - [VolunteerTimeAggregatedResponse](./Models/VolunteerTimeAggregatedResponse.md)
 - [VolunteerTimeResponse](./Models/VolunteerTimeResponse.md)
 - [VolunteerTimeUpdate](./Models/VolunteerTimeUpdate.md)
 - [VolunteerTimes_index](./Models/VolunteerTimes_index.md)
 - [VolunteerTimes_show](./Models/VolunteerTimes_show.md)
 - [WebAddress](./Models/WebAddress.md)
 - [WebAddressAggregatedResponse](./Models/WebAddressAggregatedResponse.md)
 - [WebAddressResponse](./Models/WebAddressResponse.md)
 - [WebAddressUpdate](./Models/WebAddressUpdate.md)
 - [WebAddresses_index](./Models/WebAddresses_index.md)
 - [WebAddresses_show](./Models/WebAddresses_show.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

<a name="BearerAuth"></a>
### BearerAuth

- **Type**: HTTP Bearer Token authentication

<a name="BasicAuth"></a>
### BasicAuth

- **Type**: HTTP basic authentication

<a name="ApiKeyQuery"></a>
### ApiKeyQuery

- **Type**: API key
- **API key parameter name**: access_token
- **Location**: URL query string

